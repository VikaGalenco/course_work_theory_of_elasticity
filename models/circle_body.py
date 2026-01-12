import numpy as np
from .body import Body
from .material_point import MaterialPoint


class CircleBody(Body):
    """Класс для представления кругового тела"""

    def __init__(self, center_x: float, center_y: float, radius: float, num_points: int = 36):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.num_points = num_points
        self.initialize_points()

    def initialize_points(self):
        """Инициализирует материальные точки на окружности"""
        angles = np.linspace(0, 2 * np.pi, self.num_points, endpoint=False)

        for angle in angles:
            x = self.center_x + self.radius * np.cos(angle)
            y = self.center_y + self.radius * np.sin(angle)

            # Проверяем, находится ли точка в 4-й четверти
            if x > 0 and y < 0:
                point = MaterialPoint(x, y)
                point.add_position_to_trajectory()  # Добавляем начальную позицию
                self.add_point(point)

    def get_points(self):
        return self.material_points

    def get_circle_coordinates(self):
        """
        Возвращает координаты окружности для визуализации
        """
        points = self.get_points()

        # Берем координаты материальных точек
        x_coords = [point.trajectory[0].x for point in points if point.trajectory]
        y_coords = [point.trajectory[0].y for point in points if point.trajectory]

        # Добавляем первую точку в конец (чтобы замкнуть окружность)
        if len(x_coords) > 0:
            x_coords.append(x_coords[0])
            y_coords.append(y_coords[0])

        return np.array(x_coords), np.array(y_coords)
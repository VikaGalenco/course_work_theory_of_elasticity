import numpy as np
from models.circle_body import CircleBody


class TrajectoryCalculator:
    """Класс для расчета траекторий движения тела в поле скоростей"""

    def __init__(self, body: CircleBody, t0: float = 0.0, t_end: float = 3.0):  # ИЗМЕНЕНИЕ: t0=0.0 по умолчанию
        self.body = body
        self.t0 = t0
        self.t_end = t_end

    def calculate_trajectories_analytical(self):
        """
        Аналитическое решение траекторий:
        x(t) = x₀ * exp(-[t·ln(t) - t])
        y(t) = y₀ * exp(t²/2)
        """
        points = self.body.get_points()

        for point in points:
            # Начальные координаты
            x0 = point.x
            y0 = point.y

            # Очищаем траекторию
            point.trajectory = []

            # Создаем временную сетку
            n_points = 100
            t_points = np.linspace(self.t0, self.t_end, n_points)

            for t in t_points:
                # Аналитическое решение
                if t == 0:
                    # t=0
                    x = x0
                    y = y0
                elif t > 0:
                    # x(t) = x₀ * exp(-[t·ln(t) - t])
                    # Используем безопасное вычисление для малых t
                    if t < 1e-10:
                        # При t -> 0: exp(-[t·ln(t) - t]) → exp(t) ≈ 1 + t
                        x = x0 * np.exp(t)
                    else:
                        x = x0 * np.exp(-(t * np.log(t) - t))
                    # y(t) = y₀ * exp(t²/2)
                    y = y0 * np.exp(t ** 2 / 2)
                else:
                    x = x0
                    y = y0

                # Сохраняем точку
                point.x = x
                point.y = y
                point.add_position_to_trajectory()

    def calculate_trajectories(self):
        """Рассчитывает траектории аналитически"""
        self.calculate_trajectories_analytical()

    def get_body_trajectories(self):
        """Возвращает траектории всех точек тела"""
        trajectories = []
        for point in self.body.get_points():
            x_coords = [p.x for p in point.trajectory]
            y_coords = [p.y for p in point.trajectory]
            trajectories.append((x_coords, y_coords))

        return trajectories

    def get_initial_circle(self):
        """Возвращает координаты начальной окружности"""
        return self.body.get_circle_coordinates()

    def get_form_at_time(self, t):
        """
        Возвращает форму окружности в момент времени t (аналитически)
        """
        points = self.body.get_points()
        result_x = []
        result_y = []

        for point in points:
            # Начальные координаты
            x0 = point.trajectory[0].x if point.trajectory else point.x
            y0 = point.trajectory[0].y if point.trajectory else point.y

            # Аналитическое решение для времени t
            if t == 0:
                # t=0
                x = x0
                y = y0
            elif t > 0:
                # Используем безопасное вычисление для малых t
                if t < 1e-10:
                    x = x0 * np.exp(t)
                else:
                    x = x0 * np.exp(-(t * np.log(t) - t))
                y = y0 * np.exp(t ** 2 / 2)
            else:
                x = x0
                y = y0

            result_x.append(x)
            result_y.append(y)

        return result_x, result_y

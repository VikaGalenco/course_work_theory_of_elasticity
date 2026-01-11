from .spatial_point import SpatialPoint


class MaterialPoint(SpatialPoint):
    """Класс для представления материальной точки с массой"""

    def __init__(self, x: float, y: float, mass: float = 1.0):
        super().__init__(x, y)
        self.mass = mass
        self.trajectory = []

    def add_position_to_trajectory(self):
        """Добавляет текущую позицию в траекторию"""
        self.trajectory.append(SpatialPoint(self.x, self.y))

    def get_trajectory(self):
        """Возвращает траекторию в виде массива точек"""
        return self.trajectory
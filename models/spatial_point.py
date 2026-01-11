import numpy as np


class SpatialPoint:
    """Класс для представления точки в пространстве"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"SpatialPoint({self.x:.3f}, {self.y:.3f})"

    def __add__(self, other):
        if isinstance(other, SpatialPoint):
            return SpatialPoint(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, SpatialPoint):
            return SpatialPoint(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return SpatialPoint(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def to_array(self):
        return np.array([self.x, self.y])
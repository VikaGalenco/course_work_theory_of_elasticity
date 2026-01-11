from abc import ABC, abstractmethod
from typing import List
from .material_point import MaterialPoint
from .spatial_point import SpatialPoint


class Body(ABC):
    """Абстрактный класс для представления материального тела"""

    def __init__(self, material_points: List[MaterialPoint] = None):
        self.material_points = material_points if material_points is not None else []

    @abstractmethod
    def initialize_points(self, *args, **kwargs):
        """Абстрактный метод для инициализации материальных точек тела"""
        pass

    def add_point(self, point: MaterialPoint):
        self.material_points.append(point)

    def get_points(self):
        return self.material_points

    def get_trajectories(self):
        """Возвращает траектории всех материальных точек"""
        return [point.get_trajectory() for point in self.material_points]
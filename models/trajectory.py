from typing import List
from .spatial_point import SpatialPoint
import numpy as np


class Trajectory:
    """Класс для представления траектории движения"""

    def __init__(self, points: List[SpatialPoint] = None):
        self.points = points if points is not None else []

    def add_point(self, point: SpatialPoint):
        self.points.append(point)

    def get_coordinates(self):
        """Возвращает координаты x и y отдельными массивами"""
        x_coords = [p.x for p in self.points]
        y_coords = [p.y for p in self.points]
        return np.array(x_coords), np.array(y_coords)
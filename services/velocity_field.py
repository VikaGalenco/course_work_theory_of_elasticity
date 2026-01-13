import numpy as np
from typing import Callable


class VelocityField:
    """Класс для представления поля скоростей"""

    @staticmethod
    def get_velocity(t: float, x: float, y: float) -> tuple:
        """
        Возвращает компоненты скорости в точке (x, y) в момент времени t
        """
        # Обработка особых случаев
        if t <= 0:
            return 0.0, 0.0

        vx = -np.log(t) * x
        vy = t * y

        return vx, vy

    @staticmethod
    def get_velocity_function() -> Callable:
        """
        Возвращает функцию скорости, совместимую с методом Рунге-Кутты
        """

        def velocity_func(t: float, state: np.ndarray) -> np.ndarray:
            x, y = state
            vx, vy = VelocityField.get_velocity(t, x, y)
            return np.array([vx, vy])

        return velocity_func

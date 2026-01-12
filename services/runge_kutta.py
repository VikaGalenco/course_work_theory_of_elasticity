import numpy as np
from typing import Callable

class RungeKuttaSolver:
    """Класс для численного интегрирования методом Рунге-Кутты"""

    def __init__(self, butcher_table):
        self.butcher_table = butcher_table
        self.a, self.b, self.c = butcher_table.get_coefficients()
        self.stages = butcher_table.get_stages()

    def solve(self, f: Callable, y0: np.ndarray, t0: float, t_end: float, dt: float) -> tuple:
        """
        Решает систему ОДУ dy/dt = f(t, y) методом Рунге-Кутты 4-го порядка
        """
        # Количество шагов
        n_steps = int((t_end - t0) / dt) + 1

        # Инициализация массивов
        t_points = np.linspace(t0, t_end, n_steps)
        y_points = np.zeros((n_steps, len(y0)))
        y_points[0] = y0

        # Интегрирование методом Рунге-Кутты 4-го порядка
        for i in range(n_steps - 1):
            t = t_points[i]
            y = y_points[i]

            # Вычисление k_i на каждой стадии
            k = np.zeros((self.stages, len(y0)))

            # Стадия 1
            k[0] = f(t, y)

            # Стадия 2
            y_temp = y + dt * self.a[1, 0] * k[0]
            k[1] = f(t + self.c[1] * dt, y_temp)

            # Стадия 3
            y_temp = y + dt * (self.a[2, 0] * k[0] + self.a[2, 1] * k[1])
            k[2] = f(t + self.c[2] * dt, y_temp)

            # Стадия 4
            y_temp = y + dt * (self.a[3, 0] * k[0] + self.a[3, 1] * k[1] + self.a[3, 2] * k[2])
            k[3] = f(t + self.c[3] * dt, y_temp)

            # Вычисление следующего значения y
            y_next = y.copy()
            for s in range(self.stages):
                y_next += dt * self.b[s] * k[s]

            y_points[i + 1] = y_next

        return t_points, y_points
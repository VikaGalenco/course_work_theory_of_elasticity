import numpy as np


class ButcherTable:
    """Класс для работы с таблицей Бутчера метода Рунге-Кутты 4-го порядка"""

    def __init__(self):
        # Таблица Бутчера из задания (4-стадийный метод)
        self.stages = 4

        # Матрица коэффициентов a
        self.a = np.array([
            [0, 0, 0, 0],
            [1 / 2, 0, 0, 0],
            [0, 1 / 2, 0, 0],
            [0, 0, 1, 0]
        ])

        # Вектор коэффициентов b (веса)
        self.b = np.array([1 / 6, 2 / 6, 2 / 6, 1 / 6])

        # Вектор коэффициентов c (узлы)
        self.c = np.array([0, 1 / 2, 1 / 2, 1])

    def get_stages(self):
        return self.stages

    def get_coefficients(self):
        return self.a, self.b, self.c

    def get_method_info(self):
        return {
            'name': 'RK4 (4-стадийный метод Рунге-Кутты 4-го порядка)',
            'stages': self.stages,
            'order': 4
        }
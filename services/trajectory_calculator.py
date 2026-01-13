import numpy as np
from models.circle_body import CircleBody
from services.runge_kutta import RungeKuttaSolver
from services.butcher_table import ButcherTable
from services.velocity_field import VelocityField


class TrajectoryCalculator:
    """Класс для расчета траекторий движения тела в поле скоростей"""

    def __init__(self, body: CircleBody, t0: float = 0.001, t_end: float = 2.0, dt: float = 0.01):
        self.body = body
        self.t0 = t0
        self.t_end = t_end
        self.dt = dt

        # Создаем решатель Рунге-Кутты
        self.butcher_table = ButcherTable()
        self.rk_solver = RungeKuttaSolver(self.butcher_table)

        # Функция скорости для метода РК
        self.velocity_func = VelocityField.get_velocity_function()

    def calculate_trajectories_numerical(self):
        """Рассчитывает траектории методом Рунге-Кутты"""
        points = self.body.get_points()

        for point in points:
            # Начальные координаты
            y0 = np.array([point.x, point.y])

            # Очищаем старую траекторию
            point.trajectory = []

            # Добавляем начальную точку
            point.add_position_to_trajectory()

            # Решаем систему ОДУ методом Рунге-Кутты
            t_points, y_points = self.rk_solver.solve(
                self.velocity_func,  # функция правых частей: [vx, vy]
                y0,  # начальные условия: [x0, y0]
                self.t0,  # начальное время
                self.t_end,  # конечное время
                self.dt  # шаг интегрирования
            )

            # Записываем траекторию (пропускаем первую точку, т.к. она уже добавлена)
            for i in range(1, len(t_points)):
                point.x = y_points[i, 0]
                point.y = y_points[i, 1]
                point.add_position_to_trajectory()

    def calculate_trajectories(self):
        """Рассчитывает траектории (используем численный метод Рунге-Кутты)"""
        self.calculate_trajectories_numerical()

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
        Возвращает форму окружности в момент времени t
        """
        points = self.body.get_points()
        result_x = []
        result_y = []

        for point in points:
            # Начальные координаты
            y0 = np.array([point.trajectory[0].x, point.trajectory[0].y])

            # Решаем до времени t
            t_points, y_points = self.rk_solver.solve(
                self.velocity_func,
                y0,
                self.t0,
                t,  # только до времени t
                self.dt
            )

            # Берем последнюю точку
            result_x.append(y_points[-1, 0])
            result_y.append(y_points[-1, 1])

        return result_x, result_y

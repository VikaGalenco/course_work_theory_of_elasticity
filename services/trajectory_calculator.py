import numpy as np
from models.circle_body import CircleBody
from services.velocity_field import VelocityField
from services.runge_kutta import RungeKuttaSolver
from services.butcher_table import ButcherTable


class TrajectoryCalculator:
    """Класс для расчета траекторий движения тела в поле скоростей"""

    def __init__(self, body: CircleBody, t0: float = 0.1, t_end: float = 3.0, dt: float = 0.01):
        self.body = body
        self.t0 = t0
        self.t_end = t_end  # Теперь до 3.0
        self.dt = dt

        # Инициализация решателя
        butcher_table = ButcherTable()
        self.solver = RungeKuttaSolver(butcher_table)

        # Функция скорости
        self.velocity_func = VelocityField.get_velocity_function()

    def calculate_trajectories(self):
        """Рассчитывает траектории всех материальных точек тела"""
        points = self.body.get_points()

        for point in points:
            # Начальные условия
            y0 = np.array([point.x, point.y])

            # Решаем систему ОДУ для материальной точки
            t_points, y_points = self.solver.solve(
                self.velocity_func, y0, self.t0, self.t_end, self.dt
            )

            # Очищаем существующую траекторию и добавляем новые точки
            point.trajectory = []
            for i in range(len(t_points)):
                point.x, point.y = y_points[i]
                point.add_position_to_trajectory()

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
        trajectories = self.get_body_trajectories()

        # Находим индекс, соответствующий времени t
        idx = min(int((t - self.t0) / self.dt),
                  len(trajectories[0][0]) - 1)

        # Координаты точек в момент времени t
        current_x = [traj_x[idx] for traj_x, _ in trajectories]
        current_y = [traj_y[idx] for _, traj_y in trajectories]

        return current_x, current_y
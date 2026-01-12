import numpy as np
import matplotlib.pyplot as plt
from services.velocity_field import VelocityField


class Visualization:
    """Класс для визуализации результатов"""

    @staticmethod
    def plot_trajectories_with_forms(trajectory_calculator):

        trajectories = trajectory_calculator.get_body_trajectories()

        plt.figure(figsize=(10, 8))

        # 1. Начальная форма
        init_circle_x, init_circle_y = trajectory_calculator.get_initial_circle()
        plt.plot(init_circle_x, init_circle_y, 'g-', linewidth=2,
                 label='Начальная форма (t=0.0)')  # ИЗМЕНЕНИЕ: фиксированная подпись

        # 2. Рисуем траектории
        for traj_x, traj_y in trajectories:
            plt.plot(traj_x, traj_y, 'b-', alpha=0.15, linewidth=0.7)

        # 3. Отмечаем начальные точки на начальной окружности
        init_x = [traj_x[0] for traj_x, _ in trajectories]
        init_y = [traj_y[0] for _, traj_y in trajectories]
        plt.scatter(init_x, init_y, c='green', s=10, alpha=0.6, zorder=5)

        # 4. Отмечаем конечные точки
        final_x = [traj_x[-1] for traj_x, _ in trajectories]
        final_y = [traj_y[-1] for _, traj_y in trajectories]
        plt.scatter(final_x, final_y, c='red', s=10, alpha=0.6, zorder=5,
                    label=f'Конечные точки (t={trajectory_calculator.t_end:.1f})')

        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title('Траектории движения окружности', fontsize=14, fontweight='bold')
        plt.legend(loc='best')
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_initial_form_only(trajectory_calculator):
        """
        График 2: Только начальная форма
        """
        plt.figure(figsize=(8, 8))

        # Начальная окружность
        init_circle_x, init_circle_y = trajectory_calculator.get_initial_circle()
        plt.plot(init_circle_x, init_circle_y, 'g-', linewidth=3,
                 label='Начальная форма (t=0.0)')

        # Точки материальных точек
        trajectories = trajectory_calculator.get_body_trajectories()
        init_x = [traj_x[0] for traj_x, _ in trajectories]
        init_y = [traj_y[0] for _, traj_y in trajectories]
        plt.scatter(init_x, init_y, c='green', s=30, alpha=0.8,
                    label='Материальные точки')

        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title('Начальная форма окружности', fontsize=14, fontweight='bold')

        plt.legend(loc='upper right')  

        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_deformed_form_at_2_only(trajectory_calculator):
        """
        График 3: Деформированная форма при t=2.0
        """
        plt.figure(figsize=(8, 8))

        # Получаем форму при t=2.0
        current_x, current_y = trajectory_calculator.get_form_at_time(2.0)

        # Рисуем деформированную форму
        plt.plot(current_x + [current_x[0]], current_y + [current_y[0]],
                 'r-', linewidth=3, label='Деформированная форма (t=2.0)')

        # Точки материальных точек
        plt.scatter(current_x, current_y, c='red', s=30, alpha=0.8,
                    label='Материальные точки')

        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title('Деформированная форма окружности', fontsize=14, fontweight='bold')
        plt.legend(loc='best')
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_velocity_field_only(t):
        """
        График 4,6,8: Поле скоростей
        """
        plt.figure(figsize=(10, 8))

        # Область
        x_range = (-10, 10)
        y_range = (-10, 10)

        # Сетка
        x = np.linspace(x_range[0], x_range[1], 20)
        y = np.linspace(y_range[0], y_range[1], 20)
        x_grid, y_grid = np.meshgrid(x, y)

        # Скорости
        vx_grid = np.zeros_like(x_grid)
        vy_grid = np.zeros_like(y_grid)

        for i in range(x_grid.shape[0]):
            for j in range(x_grid.shape[1]):
                vx, vy = VelocityField.get_velocity(t, x_grid[i, j], y_grid[i, j])
                vx_grid[i, j] = vx
                vy_grid[i, j] = vy

        # Модуль скорости
        speed = np.sqrt(vx_grid ** 2 + vy_grid ** 2)

        # Рисуем
        quiver = plt.quiver(x_grid, y_grid, vx_grid, vy_grid, speed,
                            cmap='viridis', alpha=0.8, scale=30, width=0.004)

        plt.colorbar(quiver, label='Модуль скорости', shrink=0.9)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title(f'Поле скоростей при t={t:.2f}', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.2)
        plt.xlim(x_range)
        plt.ylim(y_range)
        plt.gca().set_aspect('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_streamlines_only(t):
        """
        График 5,7,9: Линии тока
        """
        plt.figure(figsize=(10, 8))

        # Область
        x_range = (-10, 10)
        y_range = (-10, 10)

        # Плотная сетка
        x = np.linspace(x_range[0], x_range[1], 30)
        y = np.linspace(y_range[0], y_range[1], 30)
        x_grid, y_grid = np.meshgrid(x, y)

        # Скорости
        vx_grid = np.zeros_like(x_grid)
        vy_grid = np.zeros_like(y_grid)

        for i in range(x_grid.shape[0]):
            for j in range(x_grid.shape[1]):
                vx, vy = VelocityField.get_velocity(t, x_grid[i, j], y_grid[i, j])
                vx_grid[i, j] = vx
                vy_grid[i, j] = vy

        # Линии тока
        try:
            plt.streamplot(x_grid, y_grid, vx_grid, vy_grid,
                           color='blue', linewidth=1.5, density=1.5, arrowsize=1.0)
            plot_type = "Линии тока"
        except:
            plt.quiver(x_grid[::2, ::2], y_grid[::2, ::2],
                       vx_grid[::2, ::2], vy_grid[::2, ::2],
                       color='blue', alpha=0.7, scale=25, width=0.003)
            plot_type = "Векторное поле"

        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title(f'{plot_type} при t={t:.2f}', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.2)
        plt.xlim(x_range)
        plt.ylim(y_range)
        plt.gca().set_aspect('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def show_minimal_graphs(trajectory_calculator):

        print("\n" + "=" * 60)
        print("ГРАФИК 1: ТРАЕКТОРИИ С НАЧАЛЬНОЙ ФОРМОЙ")
        print("=" * 60)
        print("Показывает:")
        print("  • Начальную форму (зеленая окружность, t=0.0)")
        print("  • Траектории движения точек (синие линии)")
        print("  • Конечные положения точек (красные точки)")
        print("  • Все траектории начинаются на начальной окружности")
        Visualization.plot_trajectories_with_forms(trajectory_calculator)

        print("\n" + "=" * 60)
        print("ГРАФИК 2: НАЧАЛЬНАЯ ФОРМА (t=0.0)")  
        print("=" * 60)
        print("Показывает исходную окружность с материальными точками")
        Visualization.plot_initial_form_only(trajectory_calculator)

        print("\n" + "=" * 60)
        print("ГРАФИК 3: ДЕФОРМИРОВАННАЯ ФОРМА (t=2.0)")
        print("=" * 60)
        print("Показывает форму окружности после деформации")
        Visualization.plot_deformed_form_at_2_only(trajectory_calculator)

        # Поля скоростей и линии тока для 3 моментов времени
        times = [0.5, 1.0, 2.0]

        for i, t in enumerate(times):
            print(f"\n" + "=" * 60)
            print(f"ГРАФИК {4 + 2 * i}: ПОЛЕ СКОРОСТЕЙ ПРИ t={t:.1f}")
            print("=" * 60)
            print(f"Показывает распределение скоростей в момент времени t={t:.1f}")
            Visualization.plot_velocity_field_only(t)

            print(f"\n" + "=" * 60)
            print(f"ГРАФИК {5 + 2 * i}: ЛИНИИ ТОКА ПРИ t={t:.1f}")
            print("=" * 60)
            print(f"Показывает линии тока в момент времени t={t:.1f}")
            Visualization.plot_streamlines_only(t)

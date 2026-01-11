import numpy as np
import matplotlib.pyplot as plt
from models.circle_body import CircleBody
from services.velocity_field import VelocityField


class Visualization:
    """Класс для визуализации результатов"""

    @staticmethod
    def plot_trajectories(trajectory_calculator):
        """
        График 1: Траектории материальных точек до t=3.0
        """
        trajectories = trajectory_calculator.get_body_trajectories()

        # Определяем область для визуализации
        all_x = [coord for traj_x, _ in trajectories for coord in traj_x]
        all_y = [coord for _, traj_y in trajectories for coord in traj_y]

        x_min, x_max = min(all_x), max(all_x)
        y_min, y_max = min(all_y), max(all_y)

        # Добавляем отступы
        x_padding = 0.3 * (x_max - x_min)
        y_padding = 0.3 * (y_max - y_min)
        x_range = (x_min - x_padding, x_max + x_padding)
        y_range = (y_min - y_padding, y_max + y_padding)

        plt.figure(figsize=(12, 10))

        # Рисуем траектории всех точек
        for traj_x, traj_y in trajectories:
            plt.plot(traj_x, traj_y, 'b-', alpha=0.15, linewidth=0.8)

        # Отмечаем начальные точки
        init_x = [traj_x[0] for traj_x, _ in trajectories]
        init_y = [traj_y[0] for _, traj_y in trajectories]
        plt.scatter(init_x, init_y, c='green', s=50, alpha=0.7,
                    label='Начальные точки (t=0.1)', zorder=3)

        # Отмечаем конечные точки (t=3.0)
        final_x = [traj_x[-1] for traj_x, _ in trajectories]
        final_y = [traj_y[-1] for _, traj_y in trajectories]
        plt.scatter(final_x, final_y, c='red', s=50, alpha=0.7,
                    label='Конечные точки (t=3.0)', zorder=3)

        # Начальная форма для контекста
        init_circle_x, init_circle_y = trajectory_calculator.get_initial_circle()
        plt.plot(init_circle_x, init_circle_y, 'g--', linewidth=2,
                 alpha=0.6, label='Начальная форма')

        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.title('Траектории материальных точек окружности (t=0.1 до t=3.0)', fontsize=16, fontweight='bold')
        plt.legend(loc='best', fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.xlim(x_range)
        plt.ylim(y_range)

        plt.tight_layout()
        plt.savefig('1_trajectories.png', dpi=150, bbox_inches='tight')
        print("  График 1 сохранен: 1_trajectories.png")
        plt.show()

        return x_range, y_range

    @staticmethod
    def plot_initial_form(trajectory_calculator, x_range, y_range):
        """
        График 2: Начальная форма при t=0.1
        """
        plt.figure(figsize=(10, 10))

        # Начальная окружность
        init_circle_x, init_circle_y = trajectory_calculator.get_initial_circle()
        plt.plot(init_circle_x, init_circle_y, 'g-', linewidth=4, label='Начальная форма (t=0.1)')

        # Начальные точки
        trajectories = trajectory_calculator.get_body_trajectories()
        init_x = [traj_x[0] for traj_x, _ in trajectories]
        init_y = [traj_y[0] for _, traj_y in trajectories]
        plt.scatter(init_x, init_y, c='green', s=60, alpha=0.8, zorder=3)

        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.title('Начальная форма окружности', fontsize=16, fontweight='bold')
        plt.legend(loc='best', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.xlim(x_range)
        plt.ylim(y_range)

        plt.tight_layout()
        plt.savefig('2_initial_form.png', dpi=150, bbox_inches='tight')
        print("  График 2 сохранен: 2_initial_form.png")
        plt.show()

    @staticmethod
    def plot_deformed_form_at_time(trajectory_calculator, t, x_range, y_range):
        """
        График 3: Деформированная форма в момент времени t
        """
        plt.figure(figsize=(10, 10))

        # Получаем форму в момент времени t
        current_x, current_y = trajectory_calculator.get_form_at_time(t)

        # Рисуем деформированную форму
        plt.plot(current_x + [current_x[0]], current_y + [current_y[0]],
                 'r-', linewidth=4, label=f'Деформированная форма (t={t:.1f})')

        # Точки в момент времени t
        plt.scatter(current_x, current_y, c='red', s=60, alpha=0.8, zorder=3)

        # Начальная форма для сравнения
        init_circle_x, init_circle_y = trajectory_calculator.get_initial_circle()
        plt.plot(init_circle_x, init_circle_y, 'g--', linewidth=2,
                 alpha=0.7, label='Начальная форма (t=0.1)')

        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.title(f'Деформированная форма окружности при t={t:.1f}', fontsize=16, fontweight='bold')
        plt.legend(loc='best', fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.xlim(x_range)
        plt.ylim(y_range)

        # Добавляем информацию о деформации
        # Вычисляем примерные размеры
        width = max(current_x) - min(current_x)
        height = max(current_y) - min(current_y)

        plt.text(x_range[0] + 0.05 * (x_range[1] - x_range[0]),
                 y_range[1] - 0.05 * (y_range[1] - y_range[0]),
                 f'Размеры: {width:.1f} × {height:.1f}',
                 fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

        filename = f'3_deformed_form_t_{t:.1f}.png'
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"  График 3 сохранен: {filename}")
        plt.show()

    @staticmethod
    def plot_velocity_field_only(t, filename):
        """
        Графики 4-7: Поля скоростей
        """
        x_range = (-10, 10)
        y_range = (-10, 10)

        plt.figure(figsize=(12, 10))

        # Создаем сетку
        x = np.linspace(x_range[0], x_range[1], 30)
        y = np.linspace(y_range[0], y_range[1], 30)
        x_grid, y_grid = np.meshgrid(x, y)

        # Вычисляем скорости
        vx_grid = np.zeros_like(x_grid)
        vy_grid = np.zeros_like(y_grid)

        for i in range(x_grid.shape[0]):
            for j in range(x_grid.shape[1]):
                vx, vy = VelocityField.get_velocity(t, x_grid[i, j], y_grid[i, j])
                vx_grid[i, j] = vx
                vy_grid[i, j] = vy

        # Модуль скорости
        speed_grid = np.sqrt(vx_grid ** 2 + vy_grid ** 2)

        # Рисуем поле скоростей
        quiver = plt.quiver(x_grid, y_grid, vx_grid, vy_grid, speed_grid,
                            cmap='viridis', alpha=0.85, scale=25, width=0.005,
                            pivot='middle', minlength=0.1)

        # Цветовая шкала
        cbar = plt.colorbar(quiver, shrink=0.9)
        cbar.set_label('Модуль скорости', fontsize=13)
        cbar.ax.tick_params(labelsize=11)

        # Подписи
        plt.title(f'Поле скоростей при t={t:.2f}', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
        plt.xlim(x_range)
        plt.ylim(y_range)
        plt.gca().set_aspect('equal')
        plt.tick_params(axis='both', which='major', labelsize=12)

        # Формула
        if t > 0:
            formula = f"$v_1 = -\\ln({t:.2f})\\cdot x_1$, $v_2 = {t:.2f}\\cdot x_2$"
        else:
            formula = "$v_1 = 0$, $v_2 = 0$"

        plt.text(0.02, 0.98, formula, transform=plt.gca().transAxes,
                 fontsize=12, verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"  График сохранен: {filename}")
        plt.show()

    @staticmethod
    def plot_streamlines_only(t, filename):
        """
        Графики 8-11: Линии тока
        """
        x_range = (-10, 10)
        y_range = (-10, 10)

        plt.figure(figsize=(12, 10))

        # Плотная сетка для линий тока
        x = np.linspace(x_range[0], x_range[1], 50)
        y = np.linspace(y_range[0], y_range[1], 50)
        x_grid, y_grid = np.meshgrid(x, y)

        # Вычисляем скорости
        vx_grid = np.zeros_like(x_grid)
        vy_grid = np.zeros_like(y_grid)

        for i in range(x_grid.shape[0]):
            for j in range(x_grid.shape[1]):
                vx, vy = VelocityField.get_velocity(t, x_grid[i, j], y_grid[i, j])
                vx_grid[i, j] = vx
                vy_grid[i, j] = vy

        # Пробуем нарисовать линии тока
        try:
            strm = plt.streamplot(x_grid, y_grid, vx_grid, vy_grid,
                                  color='darkblue', linewidth=1.8,
                                  density=2.5, arrowsize=1.2,
                                  arrowstyle='->', minlength=0.3)
            plot_type = "Линии тока"

        except Exception as e:
            # Упрощенный вариант
            print(f"  Для t={t:.2f}: streamplot вызвал ошибку, используем упрощенный вариант")
            plt.quiver(x_grid[::2, ::2], y_grid[::2, ::2],
                       vx_grid[::2, ::2], vy_grid[::2, ::2],
                       color='darkblue', alpha=0.8, scale=20, width=0.004,
                       pivot='middle')
            plot_type = "Векторное поле"

        # Подписи
        plt.title(f'{plot_type} при t={t:.2f}', fontsize=16, fontweight='bold', pad=15)
        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
        plt.xlim(x_range)
        plt.ylim(y_range)
        plt.gca().set_aspect('equal')
        plt.tick_params(axis='both', which='major', labelsize=12)

        # Формула
        if t > 0:
            formula = f"$v_1 = -\\ln({t:.2f})\\cdot x_1$, $v_2 = {t:.2f}\\cdot x_2$"
        else:
            formula = "$v_1 = 0$, $v_2 = 0$"

        plt.text(0.02, 0.98, formula, transform=plt.gca().transAxes,
                 fontsize=12, verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"  График сохранен: {filename}")
        plt.show()

    @staticmethod
    def plot_all_graphs(trajectory_calculator):
        """
        Создает все графики:
        1. Траектории до t=3.0
        2. Начальная форма
        3. Деформированная форма при t=2.0 и t=3.0
        4-11. Поля скоростей и линии тока при t=0.5, 1.0, 2.0, 3.0
        """
        print("\n" + "=" * 60)
        print("СОЗДАНИЕ ГРАФИКОВ")
        print("=" * 60)

        print("\n[1-3] Графики траекторий и форм:")
        print("-" * 50)

        # График 1: Траектории
        print("\n1. Траектории материальных точек (t=0.1 до t=3.0)")
        x_range, y_range = Visualization.plot_trajectories(trajectory_calculator)

        # График 2: Начальная форма
        print("\n2. Начальная форма (t=0.1)")
        Visualization.plot_initial_form(trajectory_calculator, x_range, y_range)

        # График 3: Деформированная форма при t=2.0
        print("\n3. Деформированная форма при t=2.0")
        Visualization.plot_deformed_form_at_time(trajectory_calculator, 2.0, x_range, y_range)

        # График 4: Деформированная форма при t=3.0
        print("\n4. Деформированная форма при t=3.0")
        Visualization.plot_deformed_form_at_time(trajectory_calculator, 3.0, x_range, y_range)

        print("\n[5-12] Графики полей скоростей и линий тока:")
        print("-" * 50)

        # Графики 5-12: Поля скоростей и линии тока в 4 момента времени
        times = [0.50, 1.00, 2.00, 3.00]

        for i, t in enumerate(times):
            velocity_filename = f'{5 + 2 * i}_velocity_t_{t:.2f}.png'
            streamlines_filename = f'{6 + 2 * i}_streamlines_t_{t:.2f}.png'

            print(f"\nМомент времени t={t:.2f}:")
            print(f"  {5 + 2 * i}. Поле скоростей: {velocity_filename}")
            print(f"  {6 + 2 * i}. Линии тока: {streamlines_filename}")

            # График поля скоростей
            Visualization.plot_velocity_field_only(t, velocity_filename)

            # График линий тока
            Visualization.plot_streamlines_only(t, streamlines_filename)

        print("\n" + "=" * 60)
        print("ВСЕ ГРАФИКИ СОЗДАНЫ!")
        print("=" * 60)
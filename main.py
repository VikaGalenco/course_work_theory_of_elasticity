import sys
import os

# Добавляем пути
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from models.circle_body import CircleBody
from services.trajectory_calculator import TrajectoryCalculator
from services.visualization import Visualization


def main():
    print("=" * 70)
    print("ДВИЖЕНИЕ ОКРУЖНОСТИ В ПОЛЕ СКОРОСТЕЙ")
    print("=" * 70)

    # Параметры
    radius = 3.0
    center_x = 5.0
    center_y = -5.0
    t0 = 0.0 
    t_end = 2.0

    print(f"\nПАРАМЕТРЫ:")
    print(f"  • Окружность: центр ({center_x}, {center_y}), радиус {radius}")
    print(f"  • Расположение: 4-я четверть (x > 0, y < 0)")
    print(f"  • Поле: v₁ = -ln(t)·x₁, v₂ = t·x₂")
    print(f"  • Время: от t={t0:.1f} до t={t_end:.1f}")
    print(f"  • Метод: аналитическое решение")

    # Создаем окружность
    print("\nСоздание окружности...")
    body = CircleBody(center_x, center_y, radius, num_points=36)
    print(f"  Количество точек: {len(body.get_points())}")

    # Создаем калькулятор
    calculator = TrajectoryCalculator(body, t0, t_end)

    # Расчет
    print("\nРасчет траекторий...")
    calculator.calculate_trajectories()
    print("✓ Готово")

    # Показ графиков
    print("\n" + "=" * 70)
    print("=" * 70)
    print("1. Траектории материальных точек")
    print("2. Начальная форма (t=0.0)")
    print("3. Деформированная форма (t=2.0)")
    print("4. Поле скоростей при t=0.5")
    print("5. Линии тока при t=0.5")
    print("6. Поле скоростей при t=1.0")
    print("7. Линии тока при t=1.0")
    print("8. Поле скоростей при t=2.0")
    print("9. Линии тока при t=2.0")

    Visualization.show_minimal_graphs(calculator)

    print("\n" + "=" * 70)
    print("ЗАВЕРШЕНО")
    print("=" * 70)


if __name__ == "__main__":

    main()

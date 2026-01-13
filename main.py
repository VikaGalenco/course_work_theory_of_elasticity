import sys
import os

# Добавляем пути
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from models.circle_body import CircleBody
from services.trajectory_calculator import TrajectoryCalculator

# Импортируем визуализацию напрямую из файла
from services.visualization import Visualization


def main():
    print("=" * 70)
    print("ДВИЖЕНИЕ ОКРУЖНОСТИ В ПОЛЕ СКОРОСТЕЙ")
    print("=" * 70)

    # Параметры
    radius = 3.0
    center_x = 5.0
    center_y = -5.0
    t0 = 0.001
    t_end = 2.0     
    dt = 0.01       # Шаг интегрирования

    print(f"\nПАРАМЕТРЫ:")
    print(f"  • Окружность: центр ({center_x}, {center_y}), радиус {radius}")
    print(f"  • Расположение: 4-я четверть (x > 0, y < 0)")
    print(f"  • Поле: v₁ = -ln(t)·x₁, v₂ = t·x₂")
    print(f"  • Время: от t={t0:.4f} до t={t_end:.1f}")
    print(f"  • Метод: Рунге-Кутты 4-го порядка с таблицей Бутчера")
    print(f"  • Шаг интегрирования: dt={dt}")

    # Создаем окружность
    print("\nСоздание окружности...")
    body = CircleBody(center_x, center_y, radius, num_points=36)
    print(f"  Количество точек: {len(body.get_points())}")

    # Создаем калькулятор
    calculator = TrajectoryCalculator(body, t0, t_end, dt)

    # Расчет методом Рунге-Кутты
    print("\nРасчет траекторий методом Рунге-Кутты...")
    calculator.calculate_trajectories()
    print("✓ Готово")

    # Показ графиков
    print("\n" + "=" * 70)
    print("=" * 70)
    print("1. Траектории материальных точек")
    print("2. Начальная форма")
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

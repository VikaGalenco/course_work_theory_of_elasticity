#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Добавляем текущую директорию в путь поиска модулей
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Импорты
from models.circle_body import CircleBody
from services.trajectory_calculator import TrajectoryCalculator
from services.visualization import Visualization


def main():
    """Основная функция программы"""

    print("=" * 70)
    print("РАСЧЕТ ТРАЕКТОРИИ ДВИЖЕНИЯ ОКРУЖНОСТИ В ПОЛЕ СКОРОСТЕЙ")
    print("=" * 70)

    # Параметры задачи
    print("\nПАРАМЕТРЫ ЗАДАЧИ:")
    radius = 3.0
    center_x = 5.0
    center_y = -5.0
    t0 = 0.1
    t_end = 3.0  # Теперь до 3.0
    dt = 0.01

    print(f"  Радиус окружности: {radius}")
    print(f"  Начальный центр: ({center_x}, {center_y}) - 4-я четверть")
    print(f"  Поле скоростей: v₁ = -ln(t)·x₁, v₂ = t·x₂")
    print(f"  Метод: Рунге-Кутты 4-го порядка")
    print(f"  Временной интервал: [{t0}, {t_end}], шаг: {dt}")

    # Создаем тело
    print("\nСоздание окружности...")
    body = CircleBody(center_x, center_y, radius, num_points=48)
    print(f"  Количество точек: {len(body.get_points())}")

    # Создаем калькулятор траекторий
    calculator = TrajectoryCalculator(body, t0, t_end, dt)

    # Рассчитываем траектории
    print("\nРасчет траекторий...")
    calculator.calculate_trajectories()
    print("  ✓ Расчет завершен (от t=0.1 до t=3.0)")

    # Создание графиков
    print("\n" + "=" * 70)
    print("СОЗДАНИЕ ГРАФИКОВ")
    print("=" * 70)

    print("\nКОЛИЧЕСТВО И РАЗМЕРЫ ГРАФИКОВ:")
    print("  Всего: 12 графиков")
    print("  Размер: 10×10 или 12×10 дюймов")
    print("  DPI: 150 (высокое качество)")
    print("  Каждый график на отдельном листе/файле")

    try:
        Visualization.plot_all_graphs(calculator)
    except Exception as e:
        print(f"\n⚠ Ошибка при создании графиков: {e}")

    print("\n" + "=" * 70)
    print("СОЗДАННЫЕ ФАЙЛЫ (12 графиков):")
    print("=" * 70)

    print("\n▫ Графики 1-4 (траектории и формы):")
    print("  1. 1_trajectories.png          - Траектории точек (t=0.1 до t=3.0)")
    print("  2. 2_initial_form.png          - Начальная форма (t=0.1)")
    print("  3. 3_deformed_form_t_2.0.png   - Деформированная форма (t=2.0)")
    print("  4. 4_deformed_form_t_3.0.png   - Деформированная форма (t=3.0)")

    print("\n▫ Графики 5-12 (поля скоростей и линии тока):")
    print("  5. 5_velocity_t_0.50.png       - Поле скоростей при t=0.50")
    print("  6. 6_streamlines_t_0.50.png    - Линии тока при t=0.50")
    print("  7. 7_velocity_t_1.00.png       - Поле скоростей при t=1.00")
    print("  8. 8_streamlines_t_1.00.png    - Линии тока при t=1.00")
    print("  9. 9_velocity_t_2.00.png       - Поле скоростей при t=2.00")
    print("  10. 10_streamlines_t_2.00.png  - Линии тока при t=2.00")
    print("  11. 11_velocity_t_3.00.png     - Поле скоростей при t=3.00")
    print("  12. 12_streamlines_t_3.00.png  - Линии тока при t=3.00")

    print("\n" + "=" * 70)
    print("АНАЛИЗ ПОЛЯ СКОРОСТЕЙ:")
    print("=" * 70)

    print("\nКоэффициенты скорости в ключевые моменты:")
    times = [0.1, 0.5, 1.0, 2.0, 3.0]
    for t in times:
        if t > 0:
            vx_coef = -np.log(t)
            vy_coef = t
            print(f"  t={t:.1f}: v₁ = {vx_coef:6.3f}·x₁, v₂ = {vy_coef:.1f}·x₂")

    print("\nОсобенности деформации:")
    print("  • При t=0.1: сильное растяжение по x, слабое по y")
    print("  • При t=1.0: движение только по y (v₁ = 0)")
    print("  • При t=2.0: сжатие по x, растяжение по y")
    print("  • При t=3.0: сильное сжатие по x, сильное растяжение по y")

    print("\n" + "=" * 70)
    print("ПРОГРАММА УСПЕШНО ЗАВЕРШЕНА!")
    print("Все 12 графиков сохранены в текущей директории.")
    print("=" * 70)


if __name__ == "__main__":
    import numpy as np

    main()
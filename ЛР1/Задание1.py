import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + math.sin(0.5 * x) - 1

def chord_method(a, b, eps = 0.001):
    if f(a) * f(b) >= 0:
        raise ValueError("На интервале нет корня")
    while abs(b-a) > eps:
        a = a - (b - a) * f(a) / (f(b) - f(a))
        b = b - (a - b) * f(b) / (f(a) - f(b))
        print(b)

    return b


"""/////////////// Границы, найденные графически по графику/////////////////"""
a = 0.5
b = 1
""" ////////////////////////////////////////////////////////////"""



# Для построения графика
x = np.arange(-5, 5, 0.2)

y1 = x**2  # 1-й график
y2 =  1 - np.sin(0.5*x)   # 2-й график
y3 = x**2 + np.sin(0.5 * x) - 1  # весь график

# расчет методом хорд
root = chord_method(a, b)

# Создание фигуры с определенным размером
fig, ax = plt.subplots(figsize=(10, 6))

# Построение графиков с метками для легенды
plt.plot(x, y1, label='x²', linewidth=2.0)
plt.plot(x, y2, label='sin(0.5x-1)', linewidth=2.0)
plt.plot(x, y3, label='x² + sin(0.5x) - 1 (исходная функция)', linewidth=2.0)

# Добавление точки пересечения с осью X
plt.plot(root, 0, 'ro', markersize=10, label='Корень')

plt.grid(True)
plt.xlabel('Ось х')
plt.axhline(y=0, color='black', linewidth=1.5)
plt.ylabel('Ось y')
plt.title('1 задание')

# Добавление легенды
plt.legend()

# Вывод значений корня под графиком
fig.text(0.15, 0.02, f"Корень: {root:.3f}", fontsize=16)

# Настройка отступов
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

plt.show()
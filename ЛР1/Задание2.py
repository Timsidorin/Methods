import math
import numpy as np
import matplotlib.pyplot as plt


def f(x: float) -> float:
    return x ** 3 - 12 * x - 10


def f_prime(x):
    return 3 * x ** 2 - 12


def newton_method(x0, eps=0.001, max_iter=100) -> float:
    x_prev = x0
    for _ in range(max_iter):
        x_next = x_prev - f(x_prev) / f_prime(x_prev)
        if abs(x_next - x_prev) < eps:
            return x_next
        x_prev = x_next
    raise ValueError("Метод Ньютона не сошелся за указанное число итераций")


root = newton_method(x0=3.0)

print(f"Корень: {round(root, 3)}")
print(f"Значение функции в корне: {f(root):.6f}")

# Для построения графика
x = np.arange(-5, 5, 0.2)
y = f(x)

plt.grid(True)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.axhline(y=0, color='black', linewidth=1.5)
plt.plot(root, 0, 'ro', markersize=5, label='Корень')
plt.plot(x, y)

plt.show()

import math


def newton_method(x0, y0, eps=0.001):
    x = x0
    y = y0
    while True:
        f1 = math.cos(y + 1) + x - 0.5
        f2 = y - math.cos(x) - 3

        # Матрица Якоби
        J11 = 1
        J12 = -math.sin(y + 1)
        J21 = math.sin(x)
        J22 = 1

        # Определитель якобиана
        det_J = J11 * J22 - J12 * J21

        # Последовательные приближения
        delta_x = (f1 * J22 - (f2) * J12) / det_J
        delta_y = (f2 * J11 - (f1) * J21) / det_J

        x_new = x - delta_x
        y_new = y - delta_y

        # Условие остановки
        if abs(x_new - x) < eps and abs(y_new - y) < eps:
            return x_new, y_new
        x, y = x_new, y_new


# Начальное приближение
x0 = 0.3
y0 = 3.9553

x_newton, y_newton = newton_method(x0, y0)
print(f"Метод Ньютона: x = {x_newton:.4f}, y = {y_newton:.4f}")

import numpy as np

a = 0.5
b = 2.3
n = 5 # Для примера
precision = 0.001
max_iterations = 20


intervals = np.linspace(a, b, n+1) # отрезки


def f(x):
    return np.round(1/(x**2 + 2)**0.5, 4)

print("Расчётная таблица:\n")
print("i\tx_i\t\tf(x_i)")
print("------------------")
for i in range(n+1):
    print(f"{i}|\t{intervals[i]}|\t\t{f(intervals[i])}")

prev_formula = None
print("\n")
for _ in range(max_iterations):
    h = (b - a) / n
    intervals = np.linspace(a, b, n + 1)
    f_x_i = f(intervals)
    current_formula = h * ((f_x_i[0] + f_x_i[-1]) / 2 + sum(f_x_i[1:-1]))
    if prev_formula is not None and abs(current_formula - prev_formula) < precision:
        break
    print(f"Ответ: {np.round(current_formula, 5)}")
    prev_formula = current_formula
    n *= 2


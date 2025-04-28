import numpy as np

def f(x):
    return np.round(1/(x**2 + 2)**0.5, 4)


a, b = 0.5, 2.3
n1 = 8
h1 = (b - a) / n1
x = np.linspace(a, b, n1 + 1)
f_x = f(x)
sum_odd = 4 * np.sum(f_x[1:-1:2])  # Нечётные индексы
sum_even = 2 * np.sum(f_x[2:-1:2])  # Чётные индексы
S8 = (h1 / 3) * (f_x[0] + sum_odd + sum_even + f_x[-1])
print(f"Ответ для n = {n1}: {S8}")


n2 = 16
h2 = (b - a) / n2
x = np.linspace(a, b, n2 + 1)
f_x = f(x)
sum_odd = 4 * np.sum(f_x[1:-1:2])  # Нечётные индексы
sum_even = 2 * np.sum(f_x[2:-1:2])  # Чётные индексы
S16 = (h2 / 3) * (f_x[0] + sum_odd + sum_even + f_x[-1])
print(f"Ответ для n = {n2}: {S16}")
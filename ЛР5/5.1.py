


import numpy as np


a = 0.5
b = 2.3
n = 5 # Для примера
precision = 0.001



intervals = np.linspace(a, b, n+1) # отрезки






def f(x):
    return np.round(1/(x**2 + 2)**0.5, 4)


#
#
# print("Расчётная таблица:\n")
# print("i\tx_i\t\tf(x_i)")
# print("------------------")
# for i in range(n+1):
#     print(f"{i}|\t{intervals[i]}|\t\t{f(intervals[i])}")
#
#



for _ in range(100):
    h = (b - a) / n
    intervals = np.linspace(a, b, n + 1) # отрезки
    f_x_i =  (f(intervals))
    n*=2
    formula = h * ((intervals[0]+intervals[-1]/2) + sum(f_x_i))
    print(formula)
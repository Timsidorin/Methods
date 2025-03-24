import math


def iteration_method(x0,y0, eps=0.001) -> tuple[float, float, int]:
    x,y = x0, y0
    counter = 0
    while True:
        x_new = 0.5 - math.cos(y + 1)
        y_new = 3 + math.cos(x_new)
        if abs(x_new - x) < eps and abs(y_new - y) < eps:
            return x_new, y_new, counter
        x, y = x_new, y_new
        counter += 1


X0 = 0.3
Y0 = 3.9553

x, y,count_iterations = iteration_method(X0, Y0)

print(f"Метод итераций: x = {x:.4f}, y = {y:.4f}")
print(f"Решено за {count_iterations} итераций")

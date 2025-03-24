def iterate(x, y, z):
    x_new = (2.18 + 0.04 * y - 0.12 * z) / 0.93
    y_new = (1.41 - 0.15 * x + 0.03 * z) / 1.25
    z_new = (2.41 - 0.09 * x + 0.12 * y) / 0.87
    return x_new, y_new, z_new


eps = 0.001
x, y, z = 0, 0, 0  # начальное приближение
count = 0

while True:
    x_new, y_new, z_new = iterate(x, y, z)
    count += 1
    diff = max(abs(x_new - x), abs(y_new - y), abs(z_new - z))
    if diff < eps:
        break
    x, y, z = x_new, y_new, z_new

print(f"Число итераций: {count}")
print(f"Решение: x = {x_new:.6f}, y = {y_new:.6f}, z = {z_new:.6f}")
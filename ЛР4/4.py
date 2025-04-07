import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + 24 * x**2)

def Интерполяция_Лагранджа(x, x_nodes, y_nodes):
    n = len(x_nodes)
    result = 0.0
    for k in range(n):
        term = y_nodes[k]
        for i in range(n):
            if i != k:
                term *= (x - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
        result += term
    return result

# Параметры
n1 = 12
n2 = 27
K = 100
a, b = -1, 1

# 1. Построение интерполяционных таблиц
x_nodes_n1 = np.linspace(a, b, n1)
y_nodes_n1 = f(x_nodes_n1)

x_nodes_n2 = np.linspace(a, b, n2)
y_nodes_n2 = f(x_nodes_n2)


print("Интерполяционная таблица для n1 = 12:")
print("k\tx_k\t\tf(x_k)")
for k in range(n1):
    print(f"{k}\t{x_nodes_n1[k]:.4f}\t{y_nodes_n1[k]:.4f}")

print("\nИнтерполяционная таблица для n2 = 27 (первые 5 и последние 5 значений):")
print("k\tx_k\t\tf(x_k)")
for k in list(range(5)) + list(range(n2-5, n2)):
    print(f"{k}\t{x_nodes_n2[k]:.4f}\t{y_nodes_n2[k]:.4f}")

# 2. Построение интерполяционных полиномов g1(x) и g2(x)
x_test = np.linspace(a, b, K)

g1_values = np.array([Интерполяция_Лагранджа(x, x_nodes_n1, y_nodes_n1) for x in x_test])
g2_values = np.array([Интерполяция_Лагранджа(x, x_nodes_n2, y_nodes_n2) for x in x_test])

# 3. Погрешности p1 и p2
f_values = f(x_test)
p1 = np.max(np.abs(f_values - g1_values))
p2 = np.max(np.abs(f_values - g2_values))

print(f"\nПогрешность p1 (n1=12): {p1:.6f}")
print(f"Погрешность p2 (n2=27): {p2:.6f}")

# Графики
plt.figure(figsize=(12, 6))
plt.plot(x_test, f_values, label='f(x)', linewidth=2)
plt.plot(x_test, g1_values, '--', label=f'g1(x), n1={n1}', linewidth=1.5)
plt.plot(x_test, g2_values, '-.', label=f'g2(x), n2={n2}', linewidth=1.5)
plt.scatter(x_nodes_n1, y_nodes_n1, color='red', label='Узлы n1')
plt.scatter(x_nodes_n2, y_nodes_n2, color='green', label='Узлы n2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция Лагранжа для f(x) = 1/(1 + 24x²)')
plt.legend()
plt.grid()
plt.show()
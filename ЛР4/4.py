import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + 24 * x**2)

def Интерполяция_Лагранджа(x, x_nodes, y_nodes):
    result = 0.0
    for i in range(len(x_nodes)):
        term = y_nodes[i]
        for j in range(len(x_nodes)):
            if j != i:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

# Параметры
n1 = 12
n2 = 27
K = 100
a, b = -1, 1

# 1. Интерполяционные таблицы
x_nodes_n1 = np.linspace(a, b, n1)
y_nodes_n1 = f(x_nodes_n1)
x_nodes_n2 = np.linspace(a, b, n2)
y_nodes_n2 = f(x_nodes_n2)

print("Интерполяционная таблица для n1 = 12:")
print("n\tx_n\t\tf(x_n)")
for n in range(n1):
    print(f"{n}\t{x_nodes_n1[n]:.4f}\t{y_nodes_n1[n]:.4f}")

print("\nИнтерполяционная таблица для n2 = 27:")
print("n\tx_n\t\tf(x_n)")
for n in range(n2):
    print(f"{n}\t{x_nodes_n2[n]:.4f}\t{y_nodes_n2[n]:.4f}")


x_test = np.linspace(a, b, K)
f_values = f(x_test)
# 2. Вычисление значений интерполяционных полиномов в точках x_test
g1 = np.array([Интерполяция_Лагранджа(x, x_nodes_n1, y_nodes_n1) for x in x_test])
g2 = np.array([Интерполяция_Лагранджа(x, x_nodes_n2, y_nodes_n2) for x in x_test])

# 3. Вычисление погрешностей
p1 = np.max(np.abs(f_values - g1))
p2 = np.sqrt(np.sum((f_values - g2)**2) / K)


print(f"\nПогрешность p1 (n1=12): {p1:.6f}")
print(f"Погрешность p2 (n2=27): {p2:.6f}")

# 4. Построение графиков
plt.figure(figsize=(12, 6))
plt.plot(x_test, f_values, label='f(x)', linewidth=2)
plt.plot(x_test, g1, '--', label=f'g1(x), n1={n1}', linewidth=1.5)
plt.plot(x_test, g2, '-.', label=f'g2(x), n2={n2}', linewidth=1.5)
plt.scatter(x_nodes_n1, y_nodes_n1, color='red', label='Узлы n1')
plt.scatter(x_nodes_n2, y_nodes_n2, color='green', label='Узлы n2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция Лагранжа для f(x) = 1/(1 + 24x²)')
plt.legend()
plt.grid()
plt.show()
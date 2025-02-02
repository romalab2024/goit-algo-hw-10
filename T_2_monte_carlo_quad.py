import numpy as np
import scipy.integrate as spi

# Функція, яку інтегруємо
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2
y_min, y_max = 0, f(b)  # Обмеження по y

# Кількість випадкових точок
N = 100000

# Генеруємо випадкові точки (x, y)
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(y_min, y_max, N)

# Підрахунок точок, що знаходяться під кривою
under_curve = y_rand <= f(x_rand)
points_under_curve = np.sum(under_curve)

# Площа прямокутника
rectangle_area = (b - a) * (y_max - y_min)

# Оцінка інтегралу методом Монте-Карло
monte_carlo_integral = (points_under_curve / N) * rectangle_area

# Обчислення точного значення інтегралу через SciPy
exact_integral, error = spi.quad(f, a, b)

# Вивід результатів
print(f"Метод Монте-Карло: {monte_carlo_integral}")
print(f"Аналітичний розв’язок (SciPy quad): {exact_integral}")
print(f"Абсолютна похибка: {abs(monte_carlo_integral - exact_integral)}")

import numpy as np
import matplotlib.pyplot as plt

# 1. Задаём значения x: 400 точек от -2 до 6
x = np.linspace(-2, 6, 400)

# 2. Считаем y по формуле функции
y = x**2 - 4*x + 3

# 3. Строим график
plt.plot(x, y, label="y = x² - 4x + 3")

# 4. Оформляем
plt.axhline(0, color="black", linewidth=0.8)  # ось X
plt.axvline(0, color="black", linewidth=0.8)  # ось Y
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции")
plt.legend()

# 5. Показываем
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu cho hình trái tim
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Vẽ hình trái tim
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red', linewidth=2)
plt.fill(x, y, 'red', alpha=0.3)  # Tô màu bên trong trái tim
plt.title("Heart Shape")
plt.axis('equal')  # Đảm bảo tỷ lệ trục x và y bằng nhau
plt.axis('off')    # Tắt trục
plt.show()
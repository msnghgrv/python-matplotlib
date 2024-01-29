import matplotlib.pyplot as plt
import numpy as np

# 1. Plot of y = x^3
x1 = np.linspace(-5, 5, 100)
y1 = x1**3

plt.figure(figsize=(12, 8))

plt.subplot(231)  # Subplot for y = x^3
plt.plot(x1, y1, label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^3')
plt.legend()

# 2. Plot of sin(x) and cos(x)
x2 = np.linspace(0, 2 * np.pi, 100)
y2_sin = np.sin(x2)
y2_cos = np.cos(x2)

plt.subplot(232)  # Subplot for sin(x) and cos(x)
plt.plot(x2, y2_sin, label='sin(x)')
plt.plot(x2, y2_cos, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x) and cos(x)')
plt.legend()

# 3. Plot of tan(x) and cot(x)
x3 = np.linspace(-1.5 * np.pi, 1.5 * np.pi, 100)
y3_tan = np.tan(x3)
y3_cot = 1 / np.tan(x3)

plt.subplot(233)  # Subplot for tan(x) and cot(x)
plt.plot(x3, y3_tan, label='tan(x)')
plt.plot(x3, y3_cot, label='cot(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('tan(x) and cot(x)')
plt.legend()

# 4. Plot of y = x^2 and y = x^3
x4 = np.linspace(-5, 5, 100)
y4_x2 = x4**2
y4_x3 = x4**3

plt.subplot(234)  # Subplot for y = x^2 and y = x^3
plt.plot(x4, y4_x2, label='y = x^2')
plt.plot(x4, y4_x3, label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 and y = x^3')
plt.legend()

# 5. Plot of y = x^2 and y = x^3 with a legend
plt.subplot(235)
plt.plot(x4, y4_x2, label='y = x^2')
plt.plot(x4, y4_x3, label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 and y = x^3')
plt.legend()

# 6. Plot of y = x^2 and y = x^3 with a legend and a title
plt.subplot(236)
plt.plot(x4, y4_x2, label='y = x^2')
plt.plot(x4, y4_x3, label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 and y = x^3')
plt.legend()

# 7. Plot of y = x^2 and y = x^3 on the same plot with a legend, title, and axis labels
x7 = np.linspace(-5, 5, 100)
y7_x2 = x7**2
y7_x3 = x7**3

plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.plot(x7, y7_x2, label='y = x^2', color='blue')
plt.plot(x7, y7_x3, label='y = x^3', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 and y = x^3')
plt.legend()

# 8. Plot of y = x^2 and y = x^3 on the same plot with a legend, title, axis labels, and different colors
plt.subplot(132)
plt.plot(x7, y7_x2, label='y = x^2', color='red')
plt.plot(x7, y7_x3, label='y = x^3', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 and y = x^3')
plt.legend()

# 9. Scatter plot of y = x^2 and y = x^3 on the same plot with a legend, title, axis labels, different colors, and different markers
plt.subplot(133)
plt.scatter(x7, y7_x2, label='y = x^2', color='orange', marker='o')
plt.scatter(x7, y7_x3, label='y = x^3', color='brown', marker='x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot: y = x^2 and y = x^3')
plt.legend()

plt.tight_layout()

plt.show()


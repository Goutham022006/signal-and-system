import numpy as np
import matplotlib.pyplot as plt

def x(n):
    return (13 + 4 * n) * (n >= 0)

# Generate values for n
n_values = np.arange(-4, 11, 1)

# Calculate corresponding values for x(n)
x_values = [x(n) for n in n_values]

# Plot the graph
plt.stem(n_values, x_values, use_line_collection=True)
plt.title('Graph of x(n) = [13 + 4n]u(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()


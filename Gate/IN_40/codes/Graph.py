import numpy as np
import matplotlib.pyplot as plt

# Define the function
def X(s):
    return 2 * np.exp(-s) / (s**3)

# Generate values for s
s_values = np.linspace(0.1, 5, 100)  # Avoiding s=0 for division by zero

# Calculate X(s) for each s
X_values = X(s_values)

# import the data from the text file
data = np.loadtxt("output.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 24 terms of the data
y_n = data[:10]
highlighted_index = 1

# Plot
plt.figure(figsize=(8, 6))
plt.plot(s_values, X_values, label=r'$X(s) = \frac{2e^{-s}}{s^3}$')
plt.stem([highlighted_index], [data[highlighted_index - 1]], linefmt='r-', markerfmt='ro', basefmt=' ')
# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(range(1, len(data) + 1))
# Add legend
plt.legend()
plt.grid(True)
plt.savefig("fig1.png")


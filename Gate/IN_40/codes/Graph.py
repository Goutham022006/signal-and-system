import numpy as np
import matplotlib.pyplot as plt

# Define the function
def X(s):
    return 2 * np.exp(-s) / (s**3)

# Generate values for s
s_values = np.linspace(0.1, 5, 100)  # Avoiding s=0 for division by zero

# Calculate X(s) for each s
X_values = X(s_values)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(s_values, X_values, label=r'$X(s) = \frac{2e^{-s}}{s^3}$')
plt.xlabel('s')
plt.ylabel('X(s)')
plt.title('Plot of X(s)')
plt.legend()
plt.grid(True)
plt.savefig("fig1.png")

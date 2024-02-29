import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Ln
def calculate_L(n):
    phi = (1 + np.sqrt(5)) / 2
    psi = (1 - np.sqrt(5)) / 2
    return phi**n + psi**n

# Generating values for n
n_values = np.arange(0, 15)

# Calculating Ln for each n
L_values = calculate_L(n_values)

# Plotting
plt.plot(n_values, L_values, marker='o')
plt.xlabel('n')
plt.ylabel('$L_n$')
plt.grid(True)
plt.savefig("fig1.png")


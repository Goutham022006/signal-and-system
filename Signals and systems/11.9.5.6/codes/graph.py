import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("output.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 22 terms of the data
n = data[:22, 0]
y_n = data[:22, 1]

# plot the graph
highlight_index = 21
plt.scatter(n[highlight_index], y_n[highlight_index], color='red', marker='x', s=100)
plt.stem(n, y_n, linefmt='b-', basefmt='d-', markerfmt='ro') 
plt.axhline(y=1210, color='green', linestyle='--')
# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Graph of y(n) = [(13 + 2n)(n+1)]u(n)')
plt.grid(True)
plt.show()

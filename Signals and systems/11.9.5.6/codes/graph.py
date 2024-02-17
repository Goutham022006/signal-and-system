import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("output.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 24 terms of the data
n = data[:30, 0]
y_n = data[:30, 1]
# plot the graph
highlight_index = 21
plt.scatter(n[highlight_index], y_n[highlight_index], color='red', marker='x', s=100)
plt.stem(n, y_n, linefmt='b-', basefmt='d-', markerfmt='ro')
plt.axhline(y=1210, color='green', linestyle='--')

# Highlight the 21st term
plt.annotate('21st term', xy=(n[highlight_index], y_n[highlight_index]), xytext=(-20,30),
             textcoords='offset points', arrowprops=dict(arrowstyle='->', color='blue'))

# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

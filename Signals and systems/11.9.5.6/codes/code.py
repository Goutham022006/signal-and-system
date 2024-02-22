import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("result_terms.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 20 terms of the data
y_n = data[:24]
highlighted_index = 21
# plot the graph
plt.stem(range(1, len(data) + 1), y_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.stem([highlighted_index], [data[highlighted_index - 1]], linefmt='r-', markerfmt='ro', basefmt=' ')
plt.scatter(range(1, len(data) + 1), data, color='orange',marker='x',s=100,label=r'Analysis')
# Set labels and title
plt.xlabel('Term Number')
plt.ylabel('y(n)')
plt.xticks(range(1, len(data) + 1))
plt.title('Simulation v/s Analysis')

# Add legend
plt.legend()
plt.grid(True)
plt.savefig("fig1.png")

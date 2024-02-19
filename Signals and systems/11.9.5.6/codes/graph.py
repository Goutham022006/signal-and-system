import matplotlib.pyplot as plt

# Read data from file
with open('ap_sum_data.txt', 'r') as file:
    data = [int(line.strip()) for line in file]

# Highlighted term index (assuming 1-indexed)
highlighted_index = 22

# Plot stem graph
plt.stem(range(1, len(data) + 1), data, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.stem([highlighted_index], [data[highlighted_index - 1]], linefmt='r-', markerfmt='ro', basefmt=' ')

# Plot scatter plot
plt.scatter(range(1, len(data) + 1), data, color='orange')

plt.xlabel('Term Number')
plt.ylabel('Sum of Terms')
plt.show()


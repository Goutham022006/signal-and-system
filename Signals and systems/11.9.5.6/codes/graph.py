import matplotlib.pyplot as plt

def plot_ap_sum(data, highlight_index):
    plt.stem(range(1, len(data) + 1), data, linefmt='b-', markerfmt='bo', basefmt=' ')
    plt.stem([highlight_index], [data[highlight_index - 1]], linefmt='r-', markerfmt='ro', basefmt=' ')
    plt.xlabel('Term Number')
    plt.ylabel('Sum of Terms')
    plt.title('Sum of Terms in Arithmetic Progression')
    plt.savefig('fig1.png')

# Read data from file
with open('ap_sum_data.txt', 'r') as file:
    data = [int(line.strip()) for line in file]

# Highlighted term index (assuming 1-indexed)
highlighted_index = 22

plot_ap_sum(data, highlighted_index)


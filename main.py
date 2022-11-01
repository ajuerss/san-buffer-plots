import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np


def get_max(array):
    max_value = 0
    for value in array:
        if value > max_value:
            max_value = value
    return max_value


def print_visualization(filename: str):
    scatter_x, scatter_serving, scatter_routing, scatter_rotation = read_txt(filename)

    #plt.scatter(scatter_x, scatter_serving, c='forestgreen')
    plt.scatter(scatter_x, scatter_routing, c='firebrick')
    #plt.scatter(scatter_x, scatter_rotation, c='deepskyblue')

    plt.title('Costs depending on the buffersize')
    plt.xlabel('Buffersize')
    plt.ylabel('Costs')
    print(get_max(scatter_rotation))
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=get_max(scatter_routing), decimals=1))
    plt.savefig('./../results/scatter/Cost_Visualization_Scatter.png')
    plt.show()


def read_txt(filename: str):
    scatter_x = []
    scatter_serving = []
    scatter_routing = []
    scatter_rotation = []
    with open('./../results/' + filename + '.txt') as f:
        lines = f.readlines()
    for line in lines:
        x = line.split(",")
        scatter_x.append(int(x[0]))
        scatter_serving.append(int(x[1]))
        scatter_routing.append(int(x[2]))
        scatter_rotation.append(int(x[3]))
    return scatter_x, scatter_serving, scatter_routing, scatter_rotation


if __name__ == '__main__':
    print("Which results should be visualized?(Filename in results)")
    filename = input()
    print_visualization(filename)

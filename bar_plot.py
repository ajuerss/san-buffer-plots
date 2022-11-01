import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def create_plot(name, labels, serving_cost, rotation_cost):
    x = [1, 8, 32, 128, 512, 1024]
    x_axis = np.arange(len(x))
    color = ['dimgray', 'slategray', 'darkgray', 'lightgrey']

    plt.bar(x_axis - 0.15, serving_cost[0], 0.1, label=labels[0]+'S', color=color[0], edgecolor='black')
    plt.bar(x_axis - 0.05, serving_cost[1], 0.1, label=labels[1]+'S', color=color[1], edgecolor='black')
    plt.bar(x_axis + 0.05, serving_cost[2], 0.1, label=labels[2]+'S', color=color[2], edgecolor='black')
    plt.bar(x_axis + 0.15, serving_cost[3], 0.1, label=labels[3]+'S', color=color[3], edgecolor='black')

    plt.bar(x_axis - 0.15, rotation_cost[0], 0.1, bottom=serving_cost[0], color=color[0], alpha=0.5, edgecolor='black')
    plt.bar(x_axis - 0.05, rotation_cost[1], 0.1, bottom=serving_cost[1], color=color[1], alpha=0.5, edgecolor='black')
    plt.bar(x_axis + 0.05, rotation_cost[2], 0.1, bottom=serving_cost[2], color=color[2], alpha=0.5, edgecolor='black')
    plt.bar(x_axis + 0.15, rotation_cost[3], 0.1, bottom=serving_cost[3], color=color[3], alpha=0.5, edgecolor='black')

    plt.xticks(x_axis, x)
    plt.xlabel("Buffersizes")
    plt.ylabel("Costs")
    plt.title(name)
    plt.legend(loc='center left', fancybox=True, bbox_to_anchor=(1, 0.5), shadow=True, ncol=1)
    fig1 = plt.gcf()
    plt.show()
    #fig1.savefig(f'./../results/bar_plot/{name}.png', dpi=200, bbox_inches='tight')


if __name__ == '__main__':
    p = [0.0]
    a = [1.0]
    number_of_nodes = [1023]
    number_of_requests = 100000

    for x1 in number_of_nodes:
        for x2 in a:
            for x3 in p:
                labels = ['Distance', 'ClusterDistance', 'ClusterEdgeWeight', 'ClusterNodeByNode']
                search_cost = []
                rotation_cost = []
                for algo in range(0, 4):
                    with open(f'./../results/temporalLocality/result-{algo}-n{x1}-seq{number_of_requests}-a{x2}-p{x3}.txt') as f:
                        lines = f.readlines()
                    lines.pop(0)
                    s = []
                    r = []
                    max_value = 0
                    for line in lines:
                        arr = line.split(",")
                        if max_value == 0:
                            max_value = int(arr[1]) + int(arr[2])
                        s.append(int(arr[1])*100/max_value)
                        r.append(int(arr[2])*100/max_value)
                    search_cost.append(s)
                    rotation_cost.append(r)
                file_name = f'bar-n{x1}-seq{number_of_requests}-a{x2}-p{x3}'
                create_plot(file_name, labels, search_cost, rotation_cost)

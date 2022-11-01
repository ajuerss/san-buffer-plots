import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def create_plot(name, timestamps):
    arr = np.array(timestamps)
    unique, counts = np.unique(arr, return_counts=True)
    dic = dict(zip(unique, counts))
    keys = []
    values = []
    for key, value in dic.items():
        keys.append(key)
        values.append(value)
    print(max(keys), max(values))
    plt.bar(keys, values)
    plt.ylim([0, 500])
    plt.ylabel('Occurrences')
    plt.xlabel('Delay in Timestamps')
    plt.title(name)

    fig1 = plt.gcf()
    plt.show()
    fig1.savefig(f'./../results/bar_plot/ts/{name}.png', dpi=200, bbox_inches='tight')


if __name__ == '__main__':
    p = 0.0
    a = 1.0
    number_of_nodes = 1023
    number_of_requests = 100000

    labels = ['Distance', 'ClusterDistance', 'ClusterEdgeWeight', 'ClusterNodeByNode']
    search_cost = []
    with open(f'./../results/result-0-n{number_of_nodes}-seq{number_of_requests}-a{a}-p{p}-ts.txt') as f:
        lines = f.readlines()
    buffersizes = []
    timestamps = []
    for line in lines:
        arr = line.split(",")
        buffersizes.append(int(arr.pop(0)))
        timestamps.append([int(x) for x in arr])
    for a1 in range(1, len(buffersizes)):
        for b in range(0, len(timestamps[a1])):
            timestamps[a1][b] = int((timestamps[a1][b] - timestamps[0][b]))
    buffersizes.pop(0)
    timestamps.pop(0)
    for buffersize in range(0, len(buffersizes)):
        file_name = f'bar-timestamps-n{number_of_nodes}-seq{number_of_requests}-a{a}-p{p}-bs{buffersizes[buffersize]}'
        create_plot(file_name, timestamps[buffersize])

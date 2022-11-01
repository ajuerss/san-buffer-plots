import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import json
import ast
import random
import csv
import time



def empirical_entropy(seq):
    frequency = {}

    # count occurencies
    for element in seq:
        if element not in frequency:
            frequency[element] = 1
        else:
            frequency[element] += 1

    # divide by seq size
    for element in frequency:
        frequency[element] = frequency[element] / len(seq)

    # compute entropy
    entropy = 0
    for element in frequency:
        entropy -= frequency[element] * np.log2(frequency[element])

    return entropy


def create_data(n, m, a):
    # source: https://stackoverflow.com/questions/33331087/sampling-from-a-bounded-domain-zipf-distribution
    node_size = int((n ** 2 - n) / 2)  # number of nodes
    sequence_size = m
    x = np.arange(1, node_size + 1)

    dataset = {}

    weights = x ** (-a)
    weights /= weights.sum()
    bounded_zipf = stats.rv_discrete(name='bounded_zipf', values=(x, weights))
    dataset[a] = {}

    sample = list(bounded_zipf.rvs(size=sequence_size))

    #plt.hist(sample, bins=np.arange(1, node_size + 2))
    #plt.show()

    dataset[a] = {}
    dataset[a]['sequence'] = sample
    dataset[a]['entropy'] = empirical_entropy(sample)

    return dataset[a]['sequence']


def create_dataset(p, a, number_of_nodes, number_of_requests):
    data = create_data(number_of_nodes, number_of_requests, a)
    singular_nodes = list(range(1, int((number_of_nodes ** 2 - number_of_nodes) / 2) + 1))
    random.shuffle(singular_nodes)

    dictionary = [0] * int(((number_of_nodes ** 2 - number_of_nodes) / 2) + 1)
    for x in range(1, number_of_nodes + 1):
        for y in range(x + 1, number_of_nodes + 1):
            dictionary[singular_nodes.pop(0)] = [x, y]
    for i in range(len(data)):
        data[i] = dictionary[data[i]]

    for x in data:
        num = random.uniform(0, 1)
        if num > 0.5:
            temp = x[0]
            x[0] = x[1]
            x[1] = temp

    for d in range(len(data)-1):
        num = random.uniform(0, 1)
        if num < p:
            data[d + 1] = data[d]

    f = open(f'datasets/zipf-dataset-N{number_of_nodes}-seq{number_of_requests}-a{a}-p{p}.csv', 'w')
    writer = csv.writer(f)
    count = 1
    for d in data:
        row = [count, d[0], d[1]]
        writer.writerow(row)
        count += 1
    f.close()


if __name__ == '__main__':
    p = [0.0]
    a = [1.1]
    number_of_nodes = [127]
    number_of_requests = 100000

    for x1 in number_of_nodes:
        for x2 in a:
            for x3 in p:
                print(f'n{x1}-seq{number_of_requests}-a{x2}-p{x3}-start')
                create_dataset(x3, x2, x1, number_of_requests)
                print(f'n{x1}-seq{number_of_requests}-a{x2}-p{x3}-done')




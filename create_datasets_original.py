import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import json
import ast

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


# source: https://stackoverflow.com/questions/33331087/sampling-from-a-bounded-domain-zipf-distribution
N = 1023  # number of nodes
sequence_size = 50000
json_file_name = f"spatial-locality-zipf-dataset-N{N}-seq{sequence_size}.json"
x = np.arange(1, N + 1)
a_parameter_values = [1.001, 1.3, 1.6, 1.9, 2.2]
repetitions = 10

dataset = {}

for a in a_parameter_values:
    weights = x ** (-a)
    weights /= weights.sum()
    bounded_zipf = stats.rv_discrete(name='bounded_zipf', values=(x, weights))
    dataset[a] = {}

    # repeat 10 times
    for i in range(repetitions):
        sample = list(bounded_zipf.rvs(size=sequence_size))
        dataset[a][f'sample{i}'] = {}
        dataset[a][f'sample{i}']['sequence'] = str(sample)
        dataset[a][f'sample{i}']['entropy'] = empirical_entropy(sample)

        # plot only the 10th data distribution
    plt.hist(sample, bins=np.arange(1, N + 2))
    plt.show()

f = open(json_file_name, "w")
f.close()

with open(json_file_name, "w") as handle:
    json.dump(dataset, handle)

## loading the dataset
with open(json_file_name, "r") as handle:
    loaded_dataset = json.load(handle)

# covert sequence from string to list
for a in loaded_dataset:
    for i in range(repetitions):
        loaded_dataset[a][f'sample{i}']['sequence'] = ast.literal_eval(loaded_dataset[a][f'sample{i}']['sequence'])

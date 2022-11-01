import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import json
import ast


if __name__ == '__main__':
    # source: https://stackoverflow.com/questions/33331087/sampling-from-a-bounded-domain-zipf-distribution
    N = 255
    sequence_size = 100000
    json_file_name = f"spatial-locality-zipf-dataset-N{N}-seq{sequence_size}.json"
    x = np.arange(1, N + 1)
    a_parameter_values = [0.0, 1.0, 2.2]
    repetitions = 10

    dataset = {}

    for a in a_parameter_values:
        weights = x ** (-a)
        weights /= weights.sum()
        bounded_zipf = stats.rv_discrete(name='bounded_zipf', values=(x, weights))
        dataset[a] = {}

        sample = list(bounded_zipf.rvs(size=sequence_size))

        plt.hist(sample, bins=np.arange(1, N + 2))
        plt.show()

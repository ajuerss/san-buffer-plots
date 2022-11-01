import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import random

if __name__ == '__main__':

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot()

    sequence_containing_x_vals = list(range(0, 100))
    sequence_containing_y_vals = list(range(0, 100))

    random.shuffle(sequence_containing_x_vals)
    random.shuffle(sequence_containing_y_vals)

    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals)
    plt.show()

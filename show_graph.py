import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main(argv):
    csv_file = argv[1]
    save_graph(csv_file)


def save_graph(csv_file):
    df = pd.read_csv(csv_file)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    sold_out_df = df[df['sold_out'] == True]

    hist_data = sold_out_df['price']
    range_min = hist_data.min()
    range_max = hist_data.max()
    ax.hist(hist_data, bins=50, range=(range_min, 40000))
    fig.show()
    plt.savefig('figure.png')


if __name__ == '__main__':
    main(sys.argv)
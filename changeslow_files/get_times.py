#!/usr/bin/env python3

from changeslow_files.changeslow import changeslow
from time import time

def get_times(denoms, n):
    time_file = open("times.csv", "w")
    for i in range(1, n+1):
        t_zero = time()
        changeslow(denoms, i)
        time_file.write("{},{}\n".format(time() - t_zero, i))
    time_file.close()


if __name__ == "__main__":
    denoms_list = [
        [1, 5, 10, 25, 50]
    ]
    get_times(denoms_list[0], 22)



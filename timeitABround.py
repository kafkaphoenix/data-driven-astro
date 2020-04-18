import numpy as np
import timeit

def calc_statsA(filename):
    data = np.loadtxt(filename, delimiter=',')
    return np.mean(data).round(1), np.median(data).round(1)

def calc_statsB(filename):
    data = np.loadtxt(filename, delimiter=',')
    return np.round(np.mean(data), 1), np.round(np.median(data),1)

filename = 'data/data.csv'

if __name__ == '__main__':
    print(timeit.timeit('calc_statsA(filename)', 'from __main__ import calc_statsA, filename',number=10000))

    print(timeit.timeit('calc_statsB(filename)', 'from __main__ import calc_statsB,filename',number=10000))
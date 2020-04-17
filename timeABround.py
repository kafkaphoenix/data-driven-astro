import numpy as np
import time

def calc_statsA(filename):
    data = np.loadtxt(filename, delimiter=',')
    return np.mean(data).round(1), np.median(data).round(1)

def calc_statsB(filename):
    data = np.loadtxt(filename, delimiter=',')
    return np.round(np.mean(data), 1), np.round(np.median(data),1)

def measureTimeAB():
    start = time.time()

    print(calc_statsA('data.csv'))

    end = time.time()
    print(end - start)

    start = time.time()

    print(calc_statsB('data.csv'))

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    measureTimeAB()
  
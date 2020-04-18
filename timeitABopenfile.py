import timeit

def methodA(filename):
    data = []
    for line in open(filename):
        data.append(line.strip().split(','))

    return data

def methodB(filename):
    with open(filename) as f:
        data = f.readlines()
    
    data = [line.strip().split(',') for line in data]

    return data

filename = 'data/data.csv'

if __name__ == '__main__':
    print(timeit.timeit('methodA(filename)', 'from __main__ import methodA, filename',number=10000))

    print(timeit.timeit('methodB(filename)', 'from __main__ import methodB,filename',number=10000))
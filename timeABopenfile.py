import time

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

def measureTimeAB():
    start = time.time()

    print(methodA('data.csv'))

    end = time.time()
    print(end - start)

    start = time.time()

    print(methodB('data.csv'))

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    measureTimeAB()

# [['8.84', '17.22', '13.22', '3.84'], ['3.99', '11.73', '19.66', '1.27'], ['16.14', '18.72', '7.43', '11.09']]
# 0.0019943714141845703
# [['8.84', '17.22', '13.22', '3.84'], ['3.99', '11.73', '19.66', '1.27'], ['16.14', '18.72', '7.43', '11.09']]
# 0.0009984970092773438    
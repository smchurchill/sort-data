## sorting lists of random sizes

import quicksort as qs
import numpy as np
import random
import time
import os

file_name = 'rand_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    init_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh')
    init_data = []


def data_point(n):
    random.seed()
    d1 = random.sample(range(10000), k=n)
    t1_start = time.time()
    d2 = qs.qs(d1)
    t1 = time.time() - t1_start
    random.shuffle(d2)
    t2_start = time.time()
    garbage = qs.qs(d2)
    t2 = time.time() - t2_start
    data_point = [n, t1, t2]
    print(data_point)
    return data_point

def main():
##    Each data point describes the time it takes to quicksort (with bubbling
##    threshold of 10) a certain sample taken using python's builtin random
##    module.  The intent is to examine different sorting speeds.
##    The data collected are:
##        n: the sample size
##        t1: the time taken to sort a sample taken using random.sample
##        t2: the time taken to sort a sample taken using random.sample then shuffled with random.shuffle, and
##        t3: the time taken to resort a sample after random.shuffle.
##    we'll take samples of a random size for some period of time....
    
    loop_start = time.time()
    while True:
        random.seed()
        sample_size = random.uniform(100,10000)
        init_data.append(data_point(int(sample_size)))
        if len(init_data) % 100 == 0:
                print(len(init_data))
                np.save(file_name, init_data)

if __name__ == "__main__":
    main()

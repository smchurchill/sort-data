## this is quicksort with a short bubblesort thrown in for good measure
## we bubblesort lists of size 10 or less in the base case, and I'll be testing that tolerance too.

import random
import statistics
import time

def smaller(a,b):
    return( a if a<b else b) 

def bubblesort(ts):
    for i in range(len(ts)):
        for j in range(i,len(ts)):
            if (smaller(ts[i],ts[j])!=ts[i]):
                temp = ts[i]
                ts[i] = ts[j]
                ts[j] = temp
    return ts

def quicksort(tosort):
    if(len(tosort) <= 10):
        return bubblesort(tosort)
    pivot = m3r(tosort)
    plist = [pivot]
    lesser = []
    greater = []
    for item in tosort:
        if(item < pivot):
            lesser = lesser + [item]
        elif(item > pivot):
            greater = greater + [item]
        else:
            plist = plist + [item]
    lesser = quicksort(lesser)
    greater = quicksort(greater)
    done = lesser + plist + greater
    return done

def qs(ts):
    return quicksort(ts)

def m3r(container):
    random.seed()
    triple = random.sample(container, 3)
    m = statistics.median(triple)
    return m

def isSorted(l):
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            print('it fucked up at index {} and the offenders are {} and {}'.format(i,l[i],l[i+1]))
            return False
    return True
    
def main():
    l = random.sample(range(10000), k=1000)
    start = time.clock()
    s = quicksort(l)
    print('sort took {} seconds'.format(time.clock()-start))
    if(isSorted(s)):
        print('also it really is sorted')
    else:
        print('um i guess not')

def main(n):
    l = random.sample(range(10000), k=n)
    start = time.clock()
    s = quicksort(l)
    print('sort of {} elements took {} seconds'.format(n, time.clock()-start))
    if(isSorted(s)):
        print('also it really is sorted')
    else:
        print('um i guess not')

if __name__ == "__main__":
    i = 0
    while(1):
        i=i+10
        main(i)

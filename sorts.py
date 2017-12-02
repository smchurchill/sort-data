## this is a collection of sorting algortihm implementations.

import random
import statistics
import time

def mergesort(l):
    return False

def shellsort(l):
    return False

def heapsort(l):
    return False

def smaller(a,b):
    return( a if a<b else b) 

def bubblesort(l):
    counter = 1
    while counter < len(l):
        for i in range(len(l)-counter):
            if (smaller(l[i],l[i+1])!=l[i]):
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
        counter = counter + 1
    return l

def quicksort(l,k):
    if(len(l) <= 10):
        return bubblesort(l)
    pivot = l[0]
    if k:
        pivot = sample_median(l,k)
    plist = [pivot]
    lesser = []
    greater = []
    for item in l:
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

## Convenience call for quicksort choosing pivots as the median of a sample of 3 elements
def qs3(l):
    return quicksort(l,3)

## Convenience call for quicksort choosing pivots as the median of a sample of 7 elements
def qs7(l):
    return quicksort(l,7)

## Convenience call for quicksort choosing pivots as the first element of the list
def qs0(l):
    return quicksort(l,0)

def sample_median(l,k):
    random.seed()
    ktuple = random.sample(l,k)
    m = statistics.median(ktuple)
    return m

def isSorted(l):
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            print('it messed up at index {} and the offenders are {} and {}'.format(i,l[i],l[i+1]))
            return False
    return True
    
def main():
    return False

if __name__ == "__main__":
    main()

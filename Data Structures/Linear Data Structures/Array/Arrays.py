'''

Array common methods

'''


import random


def basicArray(n, reverse=False):
    if reverse:
        return [i for i in range(n,-1,-1)]
    return [i for i in range(n)]

def randomArray(arrSize, arrMin=0, arrMax=100):
    return random.sample(range(arrMin,arrMax),arrSize)

def reverseArray(array):
    return array[::-1]


def kMax(array, k):
    arrSize = len(array)
    if k<1:
        raise Exception("k cannot be less than 1")
    if k>=arrSize:
        return max(array)
    sortedArray = array.sort(reverse=True)
    return sortedArray[k-1]


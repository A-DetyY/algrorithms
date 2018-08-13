# -*- coding: utf-8 -*-

import random


def insert_sort(array):
    length = len(array)
    for j in range(1, length):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key


def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [array[p+i] for i in range(n1)]
    R = [array[q+j+1] for j in range(n2)]
    # print(p,q,r,n1,n2)
    # print("L:{}".format(L))
    # print("R:{}".format(R))
    i = 0
    j = 0
    for k in range(p, r+1):
        if i==n1 or j==n2:
            break
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
    if i==n1:
        array[k:r+1] = R[j:n2]
    else:
        array[k:r+1] = L[i:n1]


def merge_sort(array, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)


def max_heapify(array, i, heap_size):
    left = 2*i+1
    right = 2*i+2
    if left<heap_size and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right<heap_size and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest, heap_size)


def build_max_heapify(array):
    half = int((len(array)-1)/2)
    for i in range(half, -1, -1):
        max_heapify(array, i, len(array))


def heap_sort(array):
    build_max_heapify(array)
    # print(array)
    heap_size = len(array)
    for i in range(len(array)-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        max_heapify(array, 0, heap_size)


def quick_sort(array):
    if len(array)== 1 or len(array)==0:
        return array
    value = array[0]
    small = [v for v in array if v<=value]
    large = [v for v in array if v>value]
    small.pop(0)
    # print("small:{}".format(small))
    # print("large:{}".format(large))
    return quick_sort(small) + [value] + quick_sort(large)


if __name__ == '__main__':
    array = [random.randint(0,100) for i in range(20)]
    print(array)
    array = quick_sort(array)
    print(array)


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


if __name__ == '__main__':
    array = [random.randint(0,100) for i in range(20)]
    print(array)
    insert_sort(array)
    print(array)

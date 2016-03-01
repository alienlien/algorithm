#!/usr/bin/env python3
import math


def binary_search(in_list, x):
    length = len(in_list)
    if length == 0:
        return []

    if x < in_list[0]:
        return [-1, 0]

    if x > in_list[-1]:
        return [length-1, length]

    start = 0
    end = length
    while ((end - start) >= 2):
        middle = math.floor((start + end)/2)
        if in_list[middle] < x:
            start = middle
        else:
            end = middle

    return [start, end]

if __name__ == '__main__':
    print(binary_search([1, 2, 4, 4, 5, 6, 9], 8))

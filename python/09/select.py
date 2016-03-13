#!/usr/bin/env python3
import random


def find_i(in_list, i):
    if len(in_list) == 1:
        return in_list[0]

    idx = random.randint(0, len(in_list)-1)
    pivot = in_list[idx]
    small_part = [x for x in in_list if x < pivot]
    large_part = [x for x in in_list if x > pivot]
    if len(small_part) > i:
        return find_i(small_part, i)

    num_smaller = len(in_list) - len(large_part)
    if num_smaller < i:
        return find_i(large_part, i-num_smaller)

    return pivot


if __name__ == '__main__':
    x = [2, 5, 6, 3, 9, 1, 4, 9, 4, 6, 4, 5]
    print(x)
    print(sorted(x))
    index = 7
    print('The {0}th smallest element: {1}'.format(index, find_i(x, index)))

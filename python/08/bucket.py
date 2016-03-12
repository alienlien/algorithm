#!/usr/bin/env python3
import math
import random
import sys
sys.path.append('../02/')
from insertion import insertion_sort

LIST_LENGTH = 20


def sort(in_list):
    length = len(in_list)
    buckets = []
    for i in range(0, length):
        buckets.append([])

    for x in in_list:
        idx = int(math.floor(x * length))
        buckets[idx].append(x)

    out = []
    for x in buckets:
        out += insertion_sort(x)
    return out


if __name__ == '__main__':
    x = []
    for i in range(0, LIST_LENGTH):
        x.append(round(random.random(), 3))
    print(x)
    print(sort(x))

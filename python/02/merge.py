#!/usr/bin/env python3
import math


def sort(in_list):
    if len(in_list) == 0:
        return []

    if len(in_list) == 1:
        return in_list

    n1 = math.ceil(len(in_list)/2)
    left = sort(in_list[:n1])
    right = sort(in_list[n1:])
    return merge(left, right)


def merge(list_1, list_2):
    if len(list_1) == 0:
        return list_2

    if len(list_2) == 0:
        return list_1

    idx_1, idx_2 = 0, 0
    out = []
    while (idx_1 < len(list_1) and (idx_2 < len(list_2))):
        if list_1[idx_1] < list_2[idx_2]:
            out.append(list_1[idx_1])
            idx_1 += 1
        else:
            out.append(list_2[idx_2])
            idx_2 += 1

    if idx_1 == len(list_1):
        out = out + list_2[idx_2:]
    else:
        out = out + list_1[idx_1:]

    return out


if __name__ == '__main__':
    print(sort([2, 5, 4, 1, 6, 4, 9]))

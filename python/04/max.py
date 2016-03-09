#!/usr/bin/env python3
import math
import sys


def find_max_cross(in_list, mid):
    if len(in_list) == 1:
        return 0, 0, in_list[0]

    left_sum = -sys.maxint
    left_idx = mid
    temp_sum = 0
    for i in range(mid, -1, -1):
        temp_sum += in_list[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            left_idx = i

    right_sum = -sys.maxint
    right_idx = mid
    temp_sum = 0
    for i in range(mid+1, len(in_list)):
        temp_sum += in_list[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            right_idx = i
    return left_idx, right_idx, left_sum+right_sum


def find_max(in_list):
    if len(in_list) == 1:
        return 0, 0, in_list[0]

    mid = int(math.floor(len(in_list)/2))
    left_left, left_right, left_max = find_max(in_list[:mid])
    right_left, right_right, right_max = find_max(in_list[mid:])
    cross_left, cross_right, cross_max = find_max_cross(in_list, mid)
    if left_max > right_max:
        if left_max > cross_max:
            return left_left, left_right, left_max
        else:
            return cross_left, cross_right, cross_max
    else:
        if right_max > cross_max:
            return mid+right_left, mid+right_right, right_max
        else:
            return cross_left, cross_right, cross_max


def find_max_linear(in_list):
    if len(in_list) == 1:
        return 0, 0, in_list[0]

    last = len(in_list)-1

    min_short, max_short, sum_short = find_max_linear(in_list[:-1])

    idx = last
    sum_long = -sys.maxint
    temp_sum = 0
    for i in range(last, -1, -1):
        temp_sum += in_list[i]
        if temp_sum > sum_long:
            sum_long = temp_sum
            idx = i

    if sum_long > sum_short:
        return idx, last, sum_long
    return min_short, max_short, sum_short


if __name__ == '__main__':
    x = [-1, 4, -2, 7, -5, 6, -9]
    print(x)
    print(find_max(x))
    print(find_max_linear(x))

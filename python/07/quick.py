#!/usr/bin/env python3


def sort(in_list):
    if len(in_list) == 0 or len(in_list) == 1:
        return in_list

    idx, pivot, new_list = partition(in_list, 0, len(in_list)-1)
    small_part = sort(new_list[:idx])
    large_part = sort(new_list[idx+1:])
    return small_part + [pivot] + large_part


def partition(in_list, idx_min, idx_max):
    pivot = in_list[idx_max]
    idx = idx_min
    for i in range(idx_min, idx_max):
        if in_list[i] < pivot:
            in_list[i], in_list[idx] = in_list[idx], in_list[i]
            idx += 1
    in_list[idx], in_list[idx_max] = in_list[idx_max], in_list[idx]
    return idx, pivot, in_list


def sort_2(in_list):
    if len(in_list) <= 1:
        return in_list

    pivot = in_list[0]
    return sort_2([x for x in in_list[1:] if x < pivot]) \
        + [pivot] \
        + sort_2([x for x in in_list[1:] if x >= pivot])

if __name__ == '__main__':
    x = [2, 5, 6, 3, 9, 1, 4]
    print(x)
    print(partition(x, 0, len(x)-1))
    print(sort(x))
    print(sort_2(x))

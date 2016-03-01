#!/usr/bin/env python3


def insertion_sort(in_list):
    for i in range(1, len(in_list)):
        target = in_list[i]

        ptr = i
        while (ptr > 0) and (in_list[ptr-1] > target):
            in_list[ptr] = in_list[ptr-1]
            ptr -= 1
        in_list[ptr] = target
    return in_list


def insertion_sort_2(in_list):
    for i in range(1, len(in_list)):
        target = in_list[i]
        target_index = i
        for j in range(i-1, -1, -1):
            if in_list[j] < target:
                break

            in_list[j+1] = in_list[j]
            target_index = j
        in_list[target_index] = target
    return in_list


if __name__ == '__main__':
    print(insertion_sort([2, 5, 4, 1, 6, 4, 9]))

#!/usr/bin/env python3


def selection_sort(in_list):
    for i in range(0, len(in_list)-1):
        sub_list = list(in_list[i:])
        idx = sub_list.index(min(sub_list))
#         idx, item = find_min(sub_list)
        in_list[i], in_list[idx+i] = in_list[idx+i], in_list[i] 
    return in_list


def find_min(in_list):
    if len(in_list) == 0:
        return

    min_item = in_list[0]
    min_idx = 0
    for i in range(1, len(in_list)):
        if in_list[i] < min_item:
            min_item = in_list[i] 
            min_idx = i

    return min_idx, min_item

if __name__ == '__main__':
    print(selection_sort([2, 5, 4, 1, 6, 4, 9]))

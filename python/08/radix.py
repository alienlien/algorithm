#!/usr/bin/env python3
import count as c


BINARY_LEN = 8


def get_bit_n(x, n):
    rep = bin(x)[2:]
    rep = '0' * (BINARY_LEN - len(rep)) + rep
    return int(rep[n], base=2)


def sort(in_list):
    for i in range(BINARY_LEN-1, -1, -1):
        radix_list = [get_bit_n(x, i) for x in in_list]
        in_list = c.gen_sort_list_perm(in_list, c.gen_sort_perm(radix_list))
    return in_list


if __name__ == '__main__':
    x = [2, 5, 6, 3, 9, 1, 4, 9, 4, 6, 4, 5]
    print(x)
    print(sort(x))

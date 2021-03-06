#!/usr/bin/env python3


def gen_cdf(in_list, max_val):
    out = [0] * (max_val + 1)
    for x in in_list:
        out[x] += 1

    for i in range(1, len(out)):
        out[i] += out[i-1]
    return out


def gen_sort_perm(in_list):
    perm = [0] * len(in_list)
    cdf = gen_cdf(in_list, max(in_list))
    for i in range(len(in_list)-1, -1, -1):
        val = in_list[i]
        idx = cdf[val] - 1
        perm[i] = idx
        cdf[val] -= 1
    return perm


def gen_sort_list_perm(in_list, perm):
    out = [0] * len(in_list)
    for i in range(0, len(in_list)):
        out[perm[i]] = in_list[i]
    return out


def gen_sort_list(in_list):
    return gen_sort_list_perm(in_list, gen_sort_perm(in_list))


if __name__ == '__main__':
    x = [2, 5, 6, 3, 9, 1, 4, 9, 4, 6, 4, 5]
    print(x)
    print(gen_cdf(x, max(x)))
    print(gen_sort_list(x))
    print(gen_sort_list_perm(x, gen_sort_perm(x)))

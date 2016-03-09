#!/usr/bin/env python3
import math


class Heap:

    def __init__(self, in_list):
        self.array = in_list
        self.size = len(self.array)
        self.heap_size = self.size

    def __unicode__(self):
        return 'size={0}, heap_size={1}, array={2}'. \
            format(self.size, self.heap_size, self.array)

    def __str__(self):
        return self.__unicode__()

    def sort(self):
        for i in range(self.size-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heap_size -= 1
            heapify(self, 0)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return math.floor((i+1)/2) - 1


def heapify(heap, i):
    l_child = left(i)
    r_child = right(i)

    largest = i
    if l_child < heap.heap_size and heap.array[l_child] > heap.array[largest]:
        largest = l_child
    if r_child < heap.heap_size and heap.array[r_child] > heap.array[largest]:
        largest = r_child

    if largest != i:
        heap.array[i], heap.array[largest] = heap.array[largest], heap.array[i]
        heapify(heap, largest)


def build_heap(heap):
    heap.heap_size = heap.size
    first_leaf = int(math.floor(heap.size/2)+1)
    for i in range(first_leaf-1, -1, -1):
        heapify(heap, i)
    return heap


if __name__ == '__main__':
    x = [2, 5, 4, 3, 6, 1, 9]
    print('x = ', x)
    y = build_heap(Heap(x))
    print('y = ', y)
    y.sort()
    print('y = ', y)

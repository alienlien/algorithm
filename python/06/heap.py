#!/usr/bin/env python3
import math
maxint = 10000


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
        for i in range(self.heap_size-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heap_size -= 1
            heapify(self, 0)

    def max(self):
        return self.array[0]

    def extract_max(self):
        if self.heap_size < 1:
            return 'Heap size == 0: {0}'.format(self)
        out = self.array[0]
        self.array[0] = self.array[self.heap_size-1]
        self.heap_size -= 1
        heapify(self, 0)
        return out

    def increase_key(self, i, key):
        if self.array[i] > key:
            return 'New key({0}) is less than the original key({1})'. \
                    format(key, self.array[i])
        self.array[i] = key
        while ((i > 0) and (self.array[parent(i)] < self.array[i])):
            self.array[parent(i)], self.array[i] = \
                self.array[i], self.array[parent(i)]
            i = parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.size += 1
        if self.size == self.heap_size:
            self.array.append(-maxint)
        else:
            self.array[self.heap_size-1] = -maxint
        self.increase_key(self.heap_size-1, key)


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
    print('max:', y.max())
    print('Extract: ', y.extract_max())
    print('y = ', y)
    print('Insert: ', y.insert(100))

    y.sort()
    print('y = ', y)

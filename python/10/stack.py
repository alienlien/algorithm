#!/usr/bin/env python3
DEFAULT_CAPACITY = 10


class Stack(list):

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.top = -1
        self.capacity = capacity
        self.array = [0] * capacity
        super(Stack, self).__init__([0] * capacity)

    def is_empty(self):
        return self.top == -1

    def push(self, x):
        if self.top == len(self)-1:
            raise Exception('The stack is full')
        self.top += 1
        self[self.top] = x

    def pop(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        idx = self.top
        self.top -= 1
        return self[idx]

    def num_elements(self):
        return self.top + 1

    def __unicode__(self):
        if self.is_empty():
            content = []
        else:
            content = self[:self.num_elements()]
        return '[Stack] Top: {top}, Number of elements: {num} - {content}'.\
            format(top=self.top, num=self.num_elements(), content=content)

    def __str__(self):
        return self.__unicode__()


if __name__ == '__main__':
    x = Stack()
    x.push(10)
    x.push('test')
    print(x)

#!/usr/bin/env python3
DEFAULT_CAPACITY = 5


class StackPair(list):

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.top1 = 0
        self.top2 = capacity-1
        super(StackPair, self).__init__([0] * capacity)

    def is_empty_1(self):
        return self.top1 == 0

    def is_empty_2(self):
        return self.top2 == len(self)-1

    def is_full(self):
        return self.top1 - self.top2 == 1

    def push_1(self, x):
        if self.is_full():
            raise Exception('The stack pair is full')

        self[self.top1] = x
        self.top1 += 1

    def pop_1(self):
        if self.is_empty_1():
            return 'The stack 1 is empty: {0}'.format(self.__str__())

        val = self[self.top1]
        self.top1 -= 1
        return val

    def push_2(self, x):
        if self.is_full():
            raise Exception('The stack pair is full:', self.__str__())

        self[self.top2] = x
        self.top2 -= 1

    def pop_2(self):
        if self.is_empty_2():
            return 'The stack 2 is empty: {0}'.format(self.__str__())

        val = self[self.top2]
        self.top2 += 1
        return val

    def __str__(self):
        return '[Stack Pairs] 1: {s1}, 2: {s2}'. \
            format(s1=self[:self.top1], s2=self[self.top2+1:])

if __name__ == '__main__':
    x = StackPair(4)
    print(x)
    x.push_1('aaa')
    x.push_1('bbb')
    x.push_2('zzz')
    print(x)
    x.push_1('ccc')
    print(x.pop_2())
    print(x.pop_2())

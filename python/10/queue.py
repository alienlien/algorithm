#!/usr/bin/env python3

DEFAULT_CAPACITY = 10


class Queue(list):

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.size = 0
        super(Queue, self).__init__([0] * capacity)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity 

    def enqueue(self, x):
        if self.is_full():
            raise Exception('The queue is full: ', self)

        self[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('The queue is empty:', self.__str__())

        idx = self.head
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return self[idx]

    def __unicode__(self):
        if self.is_empty():
            content = []
        else:
            if self.head <= self.tail:
                content = self[self.head:self.tail]
            else:
                content = self[self.head:] + self[:self.tail]
        return '[Queue]: Head: {h}, Tail: {t}, Content: {c}'.\
            format(h=self.head, t=self.tail, c=content)

    def __str__(self):
        return self.__unicode__()

if __name__ == '__main__':
    x = Queue(5)
    x.enqueue(100)
    x.enqueue('test')
    x.enqueue('lala')
    x.enqueue('wuwu')
    print(x)
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x)
    x.enqueue(222)
    x.enqueue(333)
    print(x)
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())

#!/usr/bin/env python3


class Node:

    def __init__(self, data=""):
        self.data = data
        self.prev = None
        self.next = None

    def __unicode__(self):
        return '[{0}]'.format(self.data)

    def __str__(self):
        return self.__unicode__()


class List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def search(self, data):
        if self.head is None:
            return None

        node = self.head
        while (node is not None and node.data != data):
            node = node.next
        return node

    def delete(self, data):
        node = self.search(data)
        if node is None:
            raise Exception('Data [{0}] is not in the list: {1}'.format(data, self.__str__()))

    def __str__(self):
        if self.head is None:
            return 'Empty List'

        node = self.head
        s = node.__str__()
        while (node.next is not None):
            node = node.next
            s += ' -> {0}'.format(node.__str__())
        return s


if __name__ == '__main__':
    l = List()
    print(l)
    l.insert('abc')
    l.insert('xxx')
    print(l)
    l.insert('lalala')
    print(l)
    print(l.search('abc'))
    print(l.search('not_exist'))

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
        node = Node('nil')
        node.next = node
        node.prev = node
        self.nil = node

    def insert(self, data):
        node = Node(data)
        head = self.nil.next
        node.next = head
        head.prev = node
        node.prev = self.nil
        self.nil.next = node

    def search(self, data):
        node = self.nil.next
        while (node != self.nil and node.data != data):
            node = node.next
        return node

    def delete(self, data):
        node = self.search(data)
        if node is self.nil:
            raise Exception('Data [{0}] is not in the list: {1}'
                .format(data, self.__str__()))

    def __str__(self):
        if self.nil.next is None:
            return "The list is empty"

        node = self.nil.next
        s = node.__str__()
        while (node.next != self.nil):
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

# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


# 双向循环链表
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def insert_node(self, value):
        node = Node(value)
        if self.head.value is None:
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            """
            first = self.head
            for i in range(self.size-1):
                first = first.next
            first.next = node
            node.prev = first
            node.next = self.head
            self.head.prev = node
            """
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.head = node
        self.size += 1

    def delete_node(self, value):
        head = self.head
        i = 1
        while head.value != value and i <= self.size:
            head = head.next
            i += 1
        if i > self.size:
            print("not find the node that you want to delete")
        else:
            head.prev.next = head.next
            head.next.prev = head.prev
            self.size -= 1

    def search_node(self, value):
        temp = self.head
        i = 1
        while i <= self.size and temp.value != value:
            temp = temp.next
            i += 1
        if i > self.size:
            print("not find the node that you want to search")
        else:
            print("this value exist in Node {}".format(i))

    def modify_node(self, value, replace):
        temp = self.head.next
        while temp is not None and temp.value != value:
            temp = temp.next
        if temp is None:
            print("not find the node that you want to modify")
        else:
            temp.value = replace
            print("replace {} with {}".format(value, replace))

    def display(self):
        temp = self.head
        s = ''
        for i in range(self.size):
            s += "{}  ".format(temp.value)
            temp = temp.next
        print(s)


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(10, 2, -1):
        linked_list.insert_node(i)
    linked_list.display()
    linked_list.search_node(5)
    linked_list.modify_node(7, 1)
    linked_list.display()
    linked_list.delete_node(4)
    linked_list.display()
    linked_list.delete_node(11)
    linked_list.display()

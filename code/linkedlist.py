# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert_node(self, value):
        node = Node(value)
        if self.head.get_next() is None:
            self.head.set_next(node)
        else:
            node.set_next(self.head.get_next())
            self.head.set_next(node)

    def delete_node(self, value):
        head = self.head
        while head.get_next() is not None and head.get_next().get_value() != value:
            head = head.get_next()
        if head.get_next() is None:
            print("not find the node that you want to delete")
        else:
            head.set_next(head.get_next().get_next())

    def search_node(self, value):
        temp = self.head.get_next()
        pos = 1
        while temp is not None and temp.get_value() != value:
            temp = temp.get_next()
            pos += 1
        if temp is None:
            print("not find the node that you want to search")
        else:
            print("this value exist in Node {}".format(pos))

    def modify_node(self, value, replace):
        temp = self.head.get_next()
        while temp is not None and temp.get_value() != value:
            temp = temp.get_next()
        if temp is None:
            print("not find the node that you want to modify")
        else:
            temp.set_value(replace)
            print("replace {} with {}".format(value, replace))

    def display(self):
        temp = self.head.get_next()
        s = ''
        while temp is not None:
            s += "{}  ".format(temp.get_value())
            temp = temp.get_next()
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

# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def pre_order_walk(self):
        self.pre_order(self.root)

    def pre_order(self, node):
        if node is not None:
            print(node.value, end='  ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order_walk(self):
        self.in_order(self.root)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.value, end='  ')
            self.in_order(node.right)

    def post_order_walk(self):
        self.post_order(self.root)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end='  ')

    def search(self, value):
        self.tree_search(self.root, value)

    def tree_search(self, node, value):
        if node is None:
            print('not find value {}'.format(value))
        if node.value == value:
            print('find value {}'.format(value))
        elif node.value > value:
            self.tree_search(node.left, value)
        else:
            self.tree_search(node.right, value)

    def iterative_tree_search(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                print('find value {}'.format(value))
                break
        if temp is None:
            print('not find value {}'.format(value))

    def tree_insert(self, value):
        x = self.root
        y = None
        while x is not None:
            y = x
            x = x.left if value < x.value else x.right
        z = Node(value)
        if y is None:
            self.root = z
        elif value < y.value:
            y.left = z
        else:
            y.right = z

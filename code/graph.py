# -*- coding: utf-8 -*-

class ArrayGraph:
    def __init__(self, vertex, edge=0):
        self.vertex = vertex
        self.edge = edge
        array = []
        for i in range(vertex):
            array.append([0 for j in range(vertex)])
        self.array = array

    def add_edge(self, x, y, w=1):
        if x > self.vertex or y > self.vertex:
            print('out of num of vertex')
            return
        self.array[x-1][y-1] = w

    def set_array(self, array):
        self.array = array

    def BFS(self, s):
        queue = [s-1]
        already = [s-1]
        while len(queue) > 0:
            u = queue.pop(0)
            print(u, end=', ')
            for i in range(self.vertex):
                if self.array[u][i] > 0:
                    if i not in already:
                        queue.append(i)
                        already.append(i)

    def DFS(self):
        already = [False for i in range(self.vertex)]
        for i in range(self.vertex):
            if already[i] == False:
                self.DFS_VISIT(i, already)

    def DFS_VISIT(self, vertex, already):
        already[vertex] = True
        print(vertex, end=', ')
        for i in range(self.vertex):
            if self.array[vertex][i] > 0 and already[i] == False:
                self.DFS_VISIT(i, already)


class Node:
    def __init__(self, vertex_num, weight=1):
        self.vertex_num = vertex_num
        self.weight = weight
        self.next = None


class ListGraph:
    def __init__(self, vertex, edge=0):
        self.vertex = vertex
        self.edge = edge
        self.list = [Node(i+1) for i in range(vertex)]

    def add_edge(self, x, y, w=1):
        if x > self.vertex or y > self.vertex:
            print('out of num of vertex')
            return
        new_one = Node(y, w)
        new_one.next = self.list[x-1].next
        self.list[x-1].next = new_one


if __name__ == '__main__':
    vertex = 8
    edge = 9
    graph = ArrayGraph(8, 9)
    array = [[0,1,0,0,1,0,0,0],[1,0,0,0,0,1,0,0],[0,0,0,1,0,1,1,0],[0,0,1,0,0,0,1,1],
             [1,0,0,0,0,0,0,0],[0,1,1,0,0,0,1,0],[0,0,1,1,0,1,0,1],[0,0,0,1,0,0,1,0]]
    graph.set_array(array)
    graph.BFS(2)
    print()

    vertex = 6
    edge = 8
    graph = ArrayGraph(vertex, edge)
    array = [[0,1,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,1,1],
             [0,1,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,0,1]]
    graph.set_array(array)
    graph.DFS()
    print()

from math import ceil
from Constants import *

class Node:

    def __init__(self, distance, index, parent=None):
        if parent is None:
            parent = []
        self.distance = distance
        self.index = index
        self.parent = parent

    def __str__(self):
        return "Distance: " + str(self.distance) + " Station: " + stations[self.index] + " Parent: " + str(self.parent)

    def __repr__(self):
        return "Distance: " + str(self.distance) + " Station: " + stations[self.index] + " Parent: " + str(self.parent)


class PriorityQueue:

    def __init__(self, queue=None):
        if queue is None:
            queue = []
        self.queue = queue
        self.index_to_heap_index = dict()
        self.size = 0

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        return int(ceil(idx / 2) - 1)

    def min_heapify(self, index=0):
        if self.left(index) >= self.size:
            return
        min_index = index
        min_value = self.queue[index].distance
        if self.queue[self.left(index)].distance < min_value:
            min_index = self.left(index)
            min_value = self.queue[self.left(index)].distance
        if self.right(index) < self.size and self.queue[self.right(index)].distance < min_value:
            min_index = self.right(index)
        if min_index != index:
            self.index_to_heap_index[self.queue[index].index] = min_index
            self.index_to_heap_index[self.queue[min_index].index] = index
            self.queue[min_index], self.queue[index] = self.queue[index], self.queue[min_index]
            return self.min_heapify(min_index)

    def update(self, index):
        while index > 0 and self.queue[self.parent(index)].distance > self.queue[index].distance:
            self.index_to_heap_index[self.queue[self.parent(index)].index] = index
            self.index_to_heap_index[self.queue[index].index] = self.parent(index)
            self.queue[self.parent(index)], self.queue[index] = self.queue[index], self.queue[self.parent(index)]
            index = self.parent(index)

    def push(self, index, distance, parent=None):
        node = Node(distance, index, parent=parent)
        self.push_node(node)

    def push_node(self, node):
        self.queue.append(node)
        self.index_to_heap_index[node.index] = self.size
        self.update(self.size)
        self.size += 1

    def pop(self):
        self.queue[0], self.queue[self.size - 1] = self.queue[self.size - 1], self.queue[0]
        self.index_to_heap_index[self.queue[0].index] = 0
        node = self.queue[self.size - 1]
        self.queue.pop()
        self.size -= 1
        del self.index_to_heap_index[node.index]
        self.min_heapify(0)
        return node

    def decrease_key(self, index, value):
        heap_index = self.index_to_heap_index[index]
        if self.queue[heap_index].distance < value:
            return
        self.queue[heap_index].distance = value
        self.update(heap_index)

    def get_node(self, index):
        heap_index = self.index_to_heap_index[index]
        return self.queue[heap_index]

    def empty(self):
        if self.size == 0:
            return True
        return False

    def __str__(self):
        s = ''
        for i, node in enumerate(self.queue):
            s += 'Heap Index: {} Node: {}\n'.format(i, node)
        s += 'Index to Heap Index\n'
        s += str(self.index_to_heap_index)
        s += '\n'
        return s


if __name__ == "__main__":
    q = PriorityQueue()
    li = [5, 1, 0, 7, 2, 8]
    print('List', li)
    print('Pushing {}'.format(1))
    q.push(Node(1, li.index(1)))
    print(q)
    print('Pushing {}'.format(0))
    q.push(Node(0, li.index(0)))
    print(q)
    print('Pushing {}'.format(8))
    q.push(Node(8, li.index(8)))
    print(q)
    print('Pushing {}'.format(5))
    q.push(Node(5, li.index(5)))
    print(q)
    print('Pushing {}'.format(2))
    q.push(Node(2, li.index(2)))
    print(q)
    print('Pushing {}'.format(7))
    q.push(Node(7, li.index(7)))
    print(q)
    q.decrease_key(0, -1)
    print(q)
    print('1. Popping..')
    print('Element: ', q.pop())
    print('Queue:')
    print(q)
    print('2. Popping..')
    print('Element: ', q.pop())
    print('Queue:')
    print(q)
    print('3. Popping..')
    print('Element: ', q.pop())
    print('Queue:')
    print(q)
    print('4. Popping..')
    print('Element: ', q.pop())
    print('Queue:')
    print(q)

# Suppose that a number of lists is "k". At the beginning, I add one more node of value infinity at the end of every
# list. As new array that was created after changing python lists to linked lists contains the smallest element of every
# list I can build from it a minimum binary heap. Later, I swap heap root with its next element in a linked list, call
# a function which will restore a binary heap property (heapify) and this element, which was deleted, I add at the end
# of a new sorted linked list. I repeat this until I won't get node with infinity value in a root. If this happen, it
# means that this heap consists only of infinity nodes and entire new sorted linked list is complete.
# Passed all tests

from math import inf


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def left(x):
    return 2*x+1


def right(x):
    return 2*x+2


def parent(x):
    return (x-1)//2


# building a min binary heap
def build_min_heap(heap):
    n = len(heap)
    for x in range(parent(n-1), -1, -1):
        min_heapify(heap, x, n)


def min_heapify(heap, i, n):
    l = left(i)
    r = right(i)
    insert = i
    if l < n and heap[insert].val > heap[l].val:
        insert = l
    if r < n and heap[insert].val > heap[r].val:
        insert = r
    if insert is not i:
        heap[insert], heap[i] = heap[i], heap[insert]
        min_heapify(heap, insert, n)


# adding a new element with infinity value at the end of each linked list
def add_element(tab):
    for x in range(len(tab)):
        jump = tab[x]
        while jump.next:
            jump = jump.next
        h = Node(inf)
        jump.next = h


def tasks(heap):
    n = len(heap)
    add_element(heap)
    build_min_heap(heap)
    start = heap[0]
    heap[0] = heap[0].next
    start.next = None
    min_heapify(heap, 0, n)
    jump = start
    while heap[0].val != inf:
        jump.next = heap[0]
        jump = jump.next
        heap[0] = heap[0].next
        jump.next = None
        min_heapify(heap, 0, n)
    return start


tab = [[0, 1, 2, 4, 5], [0, 10, 20], [5, 15, 25]]
print(tasks(tab))

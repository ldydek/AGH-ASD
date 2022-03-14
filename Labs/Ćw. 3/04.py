# [ENG] Merging "k" sorted lists using binary heap.
# [PL] Scalanie "k" posortowanych list, używając kopca binarnego.


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def tab2list(tab):
    a, b = None, None
    for x in range(len(tab)):
        h = Node()
        h.value = tab[x]
        if not a:
            a = h
            b = h
        else:
            b.next = h
            b = b.next
    return a


def print_list(a):
    while a:
        print(a.value, end="->")
        a = a.next
    print("None")


def ex04(tab):
    k = len(tab)
    h = Node()
    jump = h
    nodes = [None] * k
    for x in range(k):
        nodes[x] = tab2list(tab[x])
    build_min_heap(nodes)
    while nodes[0]:
        jump.next = nodes[0]
        jump = jump.next
        add_to_heap(nodes, nodes[0].next)
    return h.next


def add_to_heap(heap, x):
    heap[0] = x
    min_heapify(heap, len(heap), 0)


def build_min_heap(tab):
    n = len(tab)
    for x in range(n//2-1, -1, -1):
        min_heapify(tab, n, x)
    return tab


def min_heapify(tab, n, i):
    l = 2*i + 1
    r = 2*i + 2
    lowest = i
    if l < n and tab[l] and tab[i] and tab[l].value < tab[i].value:
        lowest = l
    if r < n and tab[r] and tab[lowest] and tab[r].value < tab[lowest].value:
        lowest = r
    if tab[i] is None:
        if l < n and tab[l]:
            lowest = l
        if r < n and tab[r]:
            lowest = r
        if l < n and r < n and tab[l] and tab[r]:
            if tab[l].value < tab[r].value:
                lowest = l
            else:
                lowest = r
    if i is not lowest:
        tab[i], tab[lowest] = tab[lowest], tab[i]
        min_heapify(tab, n, lowest)


tab = [[1, 2, 4], [3, 7, 11, 115], [3, 6, 7, 13, 100, 123]]
print_list(ex04(tab))



# [ENG] Heap sort on linked lists. Implementation is similar to basic heapsort but this time I keep in the array not
# single values but references to nodes. During algorithm action I compare values of nodes and swap references if
# necessary.
# Time complexity: O(n log n)
# Space complexity: O(n) - we need python list to build a heap
# [PL] Sortowanie przez kopcowanie używając list jednokierunkowych. Implementacja jest podobna do standardowej wersji
# algorytmu, ale tym razem w liście trzymam referencje do węzłów a nie liczb rzeczywistych. Podczas działania algorytmu
# porównuję wartości węzłów i zamieniam referencje do nich jeśli to konieczne.
# Złożoność czasowa: O(n log n)
# Złożoność pamięciowa: O(n) - potrzebujemy tablicy, aby móc zbudować kopiec

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


def parent(x):
    return (x-1)//2


def build_max_heap(tab):
    n = len(tab)
    for x in range(parent(n-1), -1, -1):
        max_heapify(tab, n, x)
    return tab


def max_heapify(tab, n, x):
    l = 2*x + 1
    r = 2*x + 2
    insert = x
    if l < n and tab[l].value > tab[x].value:
        insert = l
    if r < n and tab[r].value > tab[insert].value:
        insert = r
    if x is not insert:
        tab[x], tab[insert] = tab[insert], tab[x]
        max_heapify(tab, n, insert)


def heapsort(a, tab):
    n = len(tab)
    start = a
    h = Node()
    for x in range(n):
        tab[x] = start
        start = start.next
        tab[x].next = None
    start = h
    build_max_heap(tab)
    for x in range(n-1, -1, -1):
        tab[0], tab[x] = tab[x], tab[0]
        max_heapify(tab, x, 0)
    for x in range(n):
        start.next = tab[x]
        start = start.next
    return h.next


tab = [10, 3, 2, 7, 5, 13, 4]
a = tab2list(tab)
print_list(a)
print_list(heapsort(a, tab))

# The idea is to create a min heap of size "k+1". Later, I swap the root with the next element of a list and repair 
# heap property. At the end, when I can't add any elements more I sort entire heap using heap sort and merge sorted
# list with sorted array/heap. Case when k=1 I consider differently, because it's faster to do one iteration of bubble
# sort with swapping elements, when values are not in a suitable order.
# Time complexity: O(n log k)
# Space complexity: O(k)
# Passed all tests.


def SortH(p,k):
    H = Node()
    if k == 1:
        H = bubble_sort(p)
        return H
    k += 1
    heap = [None] * k
    back, front = p, p.next
    start = H
    for x in range(k):
        if back:
            back.next = None
            heap[x] = back
            back = front
        if front:
            front = front.next
    build_min_heap(heap)
    while back:
        start.next = heap[0]
        start = start.next
        add_to_heap(heap, back)
        min_heapify(heap, k, 0)
        back = front
        if front:
            front = front.next
    heapsort(heap)
    for x in range(len(heap) - 1, -1, -1):
        if heap[x]:
            start.next = heap[x]
            start = start.next
    return H.next


def add_to_heap(heap, x):
    x.next = None
    heap[0] = x


def heapsort(tab):
    n = len(tab)
    for x in range(n-1, 0, -1):
        tab[0], tab[x] = tab[x], tab[0]
        min_heapify(tab, x, 0)
    return tab


def build_min_heap(tab):
    n = len(tab)
    for x in range(n//2-1, -1, -1):
        min_heapify(tab, n, x)
    return tab


def min_heapify(tab, n, i):
    l = 2*i + 1
    r = 2*i + 2
    lowest = i
    if l < n and tab[l] and tab[i] and tab[l].val < tab[i].val:
        lowest = l
    if r < n and tab[r] and tab[lowest] and tab[r].val < tab[lowest].val:
        lowest = r
    if i is not lowest:
        tab[i], tab[lowest] = tab[lowest], tab[i]
        min_heapify(tab, n, lowest)


def bubble_sort(p):
    H = Node()
    H.val = -10**20
    H.next = p
    back = H
    middle = p
    front = p.next
    while front:
        if middle.val > front.val:
            back.next = front
            middle.next = front.next
            front.next = middle
            back = front
            front = middle.next
        else:
            back = middle
            middle = front
            front = front.next
    return H.next

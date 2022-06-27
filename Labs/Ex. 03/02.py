# [ENG] Adding a new element to max binary heap.
# [PL] Dodawanie nowego elementu do kopca binarnego typu max.

def max_heapify(tab, n, i):
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < n and tab[l] > tab[i]:
        largest = l
    if r < n and tab[r] > tab[largest]:
        largest = r
    if i is not largest:
        tab[i], tab[largest] = tab[largest], tab[i]
        max_heapify(tab, n, largest)


def build_max_heap(tab):
    n = len(tab)
    for x in range(n//2-1, -1, -1):
        max_heapify(tab, n, x)
    return tab


def parent(x):
    if x % 2 == 0:
        return (x-2)//2
    return (x-1)//2


def ex02(tab, k):
    build_max_heap(tab)
    x = len(tab)
    tab.append(k)
    while x != 0 and tab[parent(x)] < tab[x]:
        tab[parent(x)], tab[x] = tab[x], tab[parent(x)]
        x = parent(x)
    return tab


tab = [2, 1, 15, 3, 34, 23, 4]
print(ex02(tab, 100))

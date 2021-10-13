# Sortowanie przez kopcowanie. W tym algorytmie wykorzystujemy strukturę danych zwaną kopcem binarnym. Na początku
# z podanej tablicy danych budujemy kopiec, a następnie w funkcji heapsort zamieniamy korzeń kopca, czyli największy
# element w tablicy (kopiec typu max) z ostatnim elementem i przywracamy własność kopca dla pozostałych n-1 elementów.
# Złożoność czasowa: O(n lg n)
# build_max_heap: O(n)
# oraz dodatkowo heapsort: O(n lg n) - n razy max_heapify (O (lg n)) = O(n lg n)
from math import floor


def max_heapify(tab, n, i=0):
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
    for x in range(floor(len(tab)/2)-1, -1, -1):
        max_heapify(tab, n, x)
    return tab


def heap(tab, i):
    build_max_heap(tab)
    if tab[i] > tab[floor((i-1)/2)] and i >= 0:
        tab[floor((i-1)/2)], tab[i] = tab[i], tab[floor((i-1)/2)]
        heap(tab, floor((i-1)/2))
    return tab


def heapsort(tab):
    build_max_heap(tab)
    for x in range(len(tab)-1, 0, -1):
        tab[0], tab[x] = tab[x], tab[0]
        max_heapify(tab, x, 0)
    return tab


tab3 = [39, 33, 34, 27, 24, 24, 23, 12, 13, 15]
print(tab3)
n = len(tab3)
#print(build_max_heap(tab3))
# print(heap(tab3, n-1))
print(heapsort(tab3))

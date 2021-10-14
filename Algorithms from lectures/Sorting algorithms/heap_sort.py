# [ENG] In heap sort algorithm we need an array data structure called heap. It is easy to imagine heap as a completely
# binary tree and in the last level elements are located from left to right. In min type of a binary tree value of each
# node is smaller or equal to the value of its children (or child). Building binary heap from an array is
# quite easy: from each element which is not leaf we call "heapify" function, because subtree rooted in this element
# doesn't have to be a binary heap. We repeat the same operations until we reach first element of an array. Sorting an
# array is also simple: when we have max binary heap (in the root is the greatest element) we swap this element from the
# last element in the array and call "heapify" to fix heap which now consists of one element less (or in other words -
# - now we consider subarray from first to certain element)
# Building max heap: O(n)
# Time complexity: O(n lg n), because we do "n" times "heapify" O(lg n)
# [PL] W algorytmie sortowania przez kopcowanie wykorzystujemy strukturę danych zwaną kopcem binarnym. Latwo wyobrazić
# sobie kopiec jako kompletne drzewo binarne a na ostatnim poziomie węzły są położone od lewej do prawej. Na początku
# z podanej tablicy danych budujemy kopiec. Robimy to, wywołując "heapify" dla elementów kopca, które nie są liśćmi,
# ponieważ tylko dla nich warunek kopca może nie być spełniony. Następnie w funkcji heapsort zamieniamy korzeń kopca,
# czyli największy element w tablicy (kopiec typu max) z ostatnim elementem i przywracamy własność kopca dla pozostałych
# n-1 elementów.
# Build_max_heap: O(n)
# oraz dodatkowo heapsort: O(n lg n) - n razy max_heapify (O (lg n)) = O(n lg n)
# Złożoność czasowa: O(n lg n)

def max_heapify(tab, n, i):
    l = 2*i + 1
    r = 2*i + 2
    # [ENG] l and r are indexes of left and right child of certain node (if it exists)
    # [PL] l i r to indeksy lewego i prawego dziecka dla pewnego węzła (o ile one istnieją)
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


def heapsort(tab):
    n = len(tab)
    build_max_heap(tab)
    for x in range(n-1, 0, -1):
        tab[0], tab[x] = tab[x], tab[0]
        max_heapify(tab, x, 0)
    return tab


tab = [39, 33, 34, 27, 24, 24, 23, 12, 13, 15]
print(heapsort(tab))

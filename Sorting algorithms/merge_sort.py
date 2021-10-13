# Sortowanie przez scalanie. Algorytm wykorzystuje technikę "divide and conquer" i dzieli ciąg do posortowania przy
# każdym zejściu rekurencyjnym na dwa niezależne podciągi. Gdy rekurencja się kończy, zaczyna się scalanie posortowanych
# ciągów aż otrzymamy posortowaną permutację wejściowego ciągu. Nie jestem pewien, czy algorytm nie zużywa dodatkowej
# pamięci.


from random import randint


def mergesort(T):
    def merge(tab, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        Left = [0] * (n1)
        Right = [0] * (n2)

        for i in range(0, n1):
            Left[i] = tab[left + i]

        for j in range(0, n2):
            Right[j] = tab[mid + 1 + j]

        i, j = 0, 0
        k = left

        while i < n1 and j < n2:
            if Left[i] <= Right[j]:
                tab[k] = Left[i]
                i += 1
            else:
                tab[k] = Right[j]
                j += 1
            k += 1

        while i < n1:
            tab[k] = Left[i]
            i += 1
            k += 1

        while j < n2:
            tab[k] = Right[j]
            j += 1
            k += 1

    def Merge_Sort(tab, left, right):
        if left < right:
            mid = (left + (right - 1)) // 2
            Merge_Sort(tab, left, mid)
            Merge_Sort(tab, mid + 1, right)
            merge(tab, left, mid, right)
        return T

    n = len(T)
    return Merge_Sort(T, 0, n - 1)


n = 10
T = [randint(-100, 100) for i in range(10)]
print(mergesort(T))
from math import inf


def merge_sort(tab, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(tab, p, q)
        merge_sort(tab, q+1, r)
        merge(tab, p, q, r, aux_tab)
    return tab


def merge(tab, p, q, r, aux_tab):
    n1 = q-p
    n2 = r-q-1
    aux_tab[n1+1] = inf
    aux_tab[n1+2+n2+1] = inf
    for x in range(n1+1):
        aux_tab[x] = tab[p+x]
    for x in range(n2+1):
        aux_tab[x+n1+2] = tab[q+1+x]

    i = 0
    j = n1+2
    for k in range(p, r+1):
        if aux_tab[i] < aux_tab[j]:
            tab[k] = aux_tab[i]
            i += 1
        else:
            tab[k] = aux_tab[j]
            j += 1


tab = [2, 1, 5, 3, 19, 13, 14, 20, 17]
aux_tab = [0 for _ in range(len(tab)+2)]
print(merge_sort(tab, 0, len(tab)-1))
# mergesort bez O(nlogn) dodatkowej pamięci

def merge_sort(tab):
    def reku(tab, p, r):
        if p < r:
            q = (p+r)//2
            reku(tab, p, q)
            reku(tab, q+1, r)
            merge(tab, aux_tab, p, q, r)
        return tab

    def merge(tab, aux_tab, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        a, b = p, q
        xd1, xd2 = 0, 0
        ctr = a
        while xd1 < n1 and xd2 < n2:
            if tab[a] < tab[b+1]:
                aux_tab[ctr] = tab[a]
                xd1 += 1
                ctr += 1
                a += 1
            else:
                aux_tab[ctr] = tab[b+1]
                xd2 += 1
                ctr += 1
                b += 1
        while xd1 < n1:
            aux_tab[ctr] = tab[a]
            xd1 += 1
            ctr += 1
            a += 1
        while xd2 < n2:
            aux_tab[ctr] = tab[b+1]
            xd2 += 1
            ctr += 1
            b += 1
        for x in range(p, r+1):
            tab[x] = aux_tab[x]

    n = len(tab)
    aux_tab = [None]*n
    reku(tab, 0, n-1)
    return aux_tab


tab = [4, 3, 1, 9, 3, 5, 10, 15, 2, 34, 2, 14]
print(merge_sort(tab))

# własny merge sort bez dodatkowej pamięci

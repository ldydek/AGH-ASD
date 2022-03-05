# Quicksort with O(log n) additional memory in a call stack.

def partition(tab, p, r):
    x, i = tab[r], p
    for j in range(p, r):
        if x > tab[j]:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
    tab[r], tab[i] = tab[i], tab[r]
    return i


def quicksort(tab, p, r, k):
    while p < r:
        q = partition(tab, p, r)
        if q-p > r+1-q:
            quicksort(tab, q+1, r, k+1)
            r = q - 1
        else:
            quicksort(tab, p, q-1, k+1)
            p = q + 1
    return tab


tab = [5, 1, 10, 14, 7, 4, 87, 2, 55]
print(quicksort(tab, 0, len(tab)-1, 0))

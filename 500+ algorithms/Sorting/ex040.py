# Merging overlapping intervals.
# Time complexity: O(n log n)

def overlap(x, y):
    if x[1] >= y[0]:
        return True
    return False


def ex040(tab):
    n = len(tab)
    quick_sort(tab, 0, n-1)
    solution = []
    start, stop = tab[0]
    for x in range(1, n):
        interval = (start, stop)
        if overlap(interval, tab[x]):
            stop = max(stop, tab[x][1])
        else:
            solution.append((start, stop))
            start, stop = tab[x]
    solution.append((start, stop))
    return solution


def partition(tab, p, r):
    x = tab[r]
    i = p-1
    for j in range(p, r):
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def quick_sort(tab, p, r):
    while p < r:
        q = partition(tab, p, r)
        quick_sort(tab, p, q-1)
        p = q + 1
    return tab


tab = [(1, 5), (2, 3), (4, 6), (7, 8), (8, 10), (12, 15)]
print(ex040(tab))

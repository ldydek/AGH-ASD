def inclusion(x, y):
    if x[0] <= y[0] and x[1] >= y[1]:
        return True
    return False


def partition(tab, p, r, index):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j][index] <= x[index]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[r], tab[i+1] = tab[i+1], tab[r]
    return i+1


def quicksort(tab, p, r, index):
    while p < r:
        q = partition(tab, p, r, index)
        quicksort(tab, p, q-1, index)
        p = q + 1
    return tab


def ex06(L):
    n = len(L)
    for x in range(n):
        L[x] = (L[x][0], L[x][1])
    quicksort(L, 0, len(L)-1, 0)
    for x in range(n):
        L[x] = (L[x][0], L[x][1], x)
    quicksort(L, 0, len(L)-1, 1)
    index = diff = 0
    for x in range(n):
        if x - L[x][2] >= diff:
            diff = x - L[x][2]
            index = x
    return L[index][0], L[index][1]


L = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]
print(ex06(L))

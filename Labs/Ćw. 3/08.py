# [ENG] Randomized select
# [PL] Randomizowany select

from random import randint


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def randomized_partition(tab, p, r):
    i = randint(p, r)
    tab[r], tab[i] = tab[i], tab[r]
    return partition(tab, p, r)


def randomized_select(tab, p, r, i):
    if p == r:
        return tab[p]
    q = partition(tab, p, r)
    k = q - p + 1
    if k == i:
        return tab[q]
    elif k < i:
        return randomized_select(tab, q+1, r, i-k)
    else:
        return randomized_select(tab, p, q-1, i)


tab = [3, 1, 7, 6, 2, 10, 13, 5]
print(randomized_select(tab, 0, len(tab)-1, 3))

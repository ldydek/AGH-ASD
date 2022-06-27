# LIS length - not dynamically but rather greedily with binary search
# O(n lg n) !
from math import inf


def binary_search(aux_tab, k):
    n = len(aux_tab)
    l, r = 0, n - 1
    ctr = 0
    while l < r:
        m = (l + r) // 2
        if aux_tab[m] == k:
            return
        elif aux_tab[m] > k:
            r = m - 1
            ctr = 0
        else:
            l = m + 1
            ctr = 1
    m = (l + r) // 2
    if ctr == 0:
        aux_tab[m+1] = k
    else:
        aux_tab[m] = k


def lis(tab):
    n = len(tab)
    aux_tab = [inf]
    for x in range(n):
        if tab[x] == aux_tab[0]:
            continue
        elif tab[x] < aux_tab[0]:
            aux_tab[0] = tab[x]
        elif tab[x] > aux_tab[len(aux_tab)-1]:
            aux_tab.append(tab[x])
        else:
            binary_search(aux_tab, tab[x])
    return len(aux_tab)


tab = [0, 8, 4, 12, 3, 10, 6, 14, 1, 2, 5, 13, 3, 11, 7, 15]
print(lis(tab))

# LIS - nie dynamicznie, ale badziej zachłannie wykorzystująć wyszukiwanie binarne
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
    num = aux_tab[0]
    for x in range(n):
        if tab[x] == aux_tab[0]:
            continue
        elif tab[x] < aux_tab[0]:
            aux_tab[0] = tab[x]
        elif tab[x] > num:
            aux_tab.append(tab[x])
        else:
            binary_search(aux_tab, tab[x])
        num = aux_tab[len(aux_tab)-1]
    return len(aux_tab)


tab = [3, 5, 1, 8, 2, 4, 7, 6, 1, 3]
print(lis(tab))

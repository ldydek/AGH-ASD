# Problem cięcia rozwiązywany za pomocą programowania dynamicznego metodą wstępującą. Na wejściu dostajemy tablicę
# reprezentującą ceny pręta za kawałki określonej długości i musimy tak pociąć pręt, aby zmaksymalizować nasz zysk.
# f(i) - maksymalny zysk jaki można uzyskać tnąc pręt długości i
# f(0) = 0
# Zależność rekurencyjna: f(i) = max(f(i-k) + tab[k]) dla pewnego k
# f(1) = max(f(1), f(0)+tab[1])
# f(2) = max(f(2), f(1)+tab[1], f(0)+tab[2])
# funkcja print_path wypisuje dodatkowo optymalne długości pociętych prętów generujące największy zysk
from math import inf


def rod_cutting(tab):
    n = len(tab)
    aux_tab = [0]*n
    parent = [-1]*n
    for x in range(1, n):
        xd = -inf
        for y in range(x):
            if xd < aux_tab[y]+tab[x-y]:
                xd = aux_tab[y]+tab[x-y]
                parent[x] = y
        aux_tab[x] = xd
    return print_path(parent, n-1)


def print_path(parent, x):
    set = []
    while parent[x] != -1:
        set.append(x - parent[x])
        x = parent[x]
    return set


def rod_cutting_memoizaed(prices):
    def reku(prices, n):
        nonlocal aux_tab
        xd = -inf
        if aux_tab[n] != -inf:
            return aux_tab[n]
        for x in range(1, n):
            xd = max(xd, prices[x] + reku(prices, n-x))
        xd = max(xd, aux_tab[n])
        aux_tab[n] = xd
        return xd

    n = len(prices)
    aux_tab = [-inf]*n
    aux_tab[0] = 0
    aux_tab[1] = prices[1]
    reku(prices, n-1)
    return aux_tab


tab = [0, 1, 3, 10, 2, 5]
print(rod_cutting(tab))

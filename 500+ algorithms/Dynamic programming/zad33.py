# f(i) - najdłuższy podciąg ze zmieniającymi się znakami, rozważając elementy tablicy od tab[0] do tab[i], gdzie
# tab to nasza wejściowa tablica z danymi
from math import inf


def alternate(tab):
    n = len(tab)
    aux_tab = [(1, 0)]*n
    parent = [-1]*n
    # tablica informuje nas o długości rozważanego podciągu spełniającego warunki zadania oraz którym znakiem kończy
    # się nasz rozważany podciąg
    # 1 - znak mniejszości   a < b
    # -1 - znak większości a > b
    for x in range(1, n):
        ctr = (-inf, 0)
        for y in range(x):
            if tab[y] < tab[x] and aux_tab[y][1] != 1:
                if ctr[0] < aux_tab[y][0]:
                    ctr = (aux_tab[y][0], 1)
                    parent[x] = y
            if tab[y] > tab[x] and aux_tab[y][1] != -1:
                if ctr[0] < aux_tab[y][0]:
                    ctr = (aux_tab[y][0], -1)
                    parent[x] = y
        aux_tab[x] = (ctr[0]+1, ctr[1])
    ctr, xd = -inf, -inf
    for x in range(n):
        if aux_tab[x][0] > ctr:
            ctr = aux_tab[x][0]
            xd = x
    return print_path(parent, xd, tab)


def print_path(parent, b, tab):
    set = [tab[b]]
    while parent[b] != -1:
        b = parent[b]
        set.append(tab[b])
    return set[::-1]


tab = [8, 9, 6, 4, 5, 7, 3, 2, 4]
print(alternate(tab))

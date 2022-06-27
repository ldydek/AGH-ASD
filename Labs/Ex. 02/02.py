# [ENG] Inversions number in an array.
# [PL] Liczba inwersji w tablicy.


def ex02(tab):
    n = len(tab)
    aux_tab = [0] * n
    solution = divide_and_conquer(tab, 0, n-1, aux_tab)
    return solution


def divide_and_conquer(tab, p, r, aux_tab):
    inversions = 0
    q = (p+r)//2
    if p < r:
        inversions += divide_and_conquer(tab, p, q, aux_tab)
        inversions += divide_and_conquer(tab, q+1, r, aux_tab)
        inversions += merge(tab, aux_tab, p, r)
    return inversions


def merge(tab, aux_tab, p, r):
    inversions_number = 0
    q = (p+r)//2
    xd1, xd2 = p, q + 1
    ctr = p
    while xd1 <= q and xd2 <= r:
        if tab[xd1] <= tab[xd2]:
            aux_tab[ctr] = tab[xd1]
            xd1 += 1
        else:
            aux_tab[ctr] = tab[xd2]
            xd2 += 1
            inversions_number += (q + 1 - xd1)
        ctr += 1
    while xd1 <= q:
        aux_tab[ctr] = tab[xd1]
        ctr += 1
        xd1 += 1
    while xd2 <= r:
        aux_tab[ctr] = tab[xd2]
        ctr += 1
        xd2 += 1
    for x in range(p, r+1):
        tab[x] = aux_tab[x]
    return inversions_number


tab = [4, 3, 2, 1]
print(ex02(tab))

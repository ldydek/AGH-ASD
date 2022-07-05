# [ENG] Merge sort algorithm. It uses "divide and conquer" technique and divides sequence in each recursion for two
# subsequences. When recursion ends, algorithm starts merging sorted subsequences until we'll get sorted whole sequence.
# Time complexity: O(n lg n)
# Space complexity: O(n)
# [PL] Sortowanie przez scalanie. Algorytm wykorzystuje technikę "dziel i zwyciężaj" i dzieli ciąg do posortowania przy
# każdym zejściu rekurencyjnym na dwa niezależne podciągi. Gdy rekurencja się kończy, zaczyna się scalanie posortowanych
# ciągów aż otrzymamy posortowaną permutację wejściowego ciągu.
# Złożoność czasowa: O(n lg n)
# Złożoność pamięciowa: O(n)

def merge_sort(tab):
    n = len(tab)
    aux_tab = [0] * n
    divide_and_conquer(tab, 0, n-1, aux_tab)
    return tab


def divide_and_conquer(tab, p, r, aux_tab):
    q = (p+r)//2
    if p == r:
        return
    divide_and_conquer(tab, p, q, aux_tab)
    divide_and_conquer(tab, q+1, r, aux_tab)
    merge(tab, aux_tab, p, r)


def merge(tab, aux_tab, p, r):
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


tab = [4, 3, 1, 9, 3, 5, 10, 15, 2, 34, 2, 14]
print(merge_sort(tab))

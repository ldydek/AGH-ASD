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
    def reku(tab, p, r):
        if p < r:
            q = (p+r)//2
            reku(tab, p, q)
            reku(tab, q+1, r)
            merge(tab, aux_tab, p, q, r)
        return tab

    def merge(tab, aux_tab, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        a, b = p, q
        xd1, xd2 = 0, 0
        ctr = a
        while xd1 < n1 and xd2 < n2:
            if tab[a] < tab[b+1]:
                aux_tab[ctr] = tab[a]
                xd1 += 1
                ctr += 1
                a += 1
            else:
                aux_tab[ctr] = tab[b+1]
                xd2 += 1
                ctr += 1
                b += 1
        while xd1 < n1:
            aux_tab[ctr] = tab[a]
            xd1 += 1
            ctr += 1
            a += 1
        while xd2 < n2:
            aux_tab[ctr] = tab[b+1]
            xd2 += 1
            ctr += 1
            b += 1
        for x in range(p, r+1):
            tab[x] = aux_tab[x]

    n = len(tab)
    aux_tab = [None]*n
    reku(tab, 0, n-1)
    return aux_tab


tab = [4, 3, 1, 9, 3, 5, 10, 15, 2, 34, 2, 14]
print(merge_sort(tab))

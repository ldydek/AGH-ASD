# Zadanie 5. (maximin) Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1).
# Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg
# o najmniejszej wartości (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego
# podciągu. Zadanie polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.
#
#
# Rozwiązanie: Programowaniem dynamicznym:
# f(i, j) - optymalny podział tablicy składającej się z wyrazów od 0 do i na j części
# f(i, j) = min(f(i-k, j-1), sum(tab[k+1:i+1])) dla pewnego k
# Innymi słowy znajdujemy optymalny podział tablicy i rekurencyjnie szukamy optymalnych podziałów pozostałych
# podproblemów.
# f(i, 0) = 0
# f(k, 1) = sum(tab[0:k+1])
from math import inf


def max_min(tab, k):
    n = len(tab)
    aux_tab = [[0 for _ in range(k+1)] for _ in range(n)]
    aux_tab[0][1] = tab[0]
    for x in range(1, n):
        aux_tab[x][1] = aux_tab[x-1][1] + tab[x]

    for x in range(1, n):
        for y in range(2, k+1):
            ctr = -inf
            if y <= x+1:
                for z in range(x+1):
                    ctr = max(ctr, min(aux_tab[x-z][y-1], aux_tab[x][1] - aux_tab[x-z][1]))
                aux_tab[x][y] = ctr
    return aux_tab[n-1][k]


tab = [1, 2, 4, 6, 3, 2, 10, 3, 4, 2]
print(max_min(tab, 5))

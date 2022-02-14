# Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny,
# wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1
# zamiast 5 + 5 + 5).
#
#
# f(i, j) - minimalna ilość monet potrzebnych do wydania kwoty j posiadająć i pierwszych monet
# f(i, j) = min(f(i-1), j), f(i-1, j-A[i])
# f(0, j) = inf
# f(1, j) = 1 if i is in A
# Rozwiązanie: f(i) - minimalna ilość monet potrzebnych do wydania kwoty i
from math import inf


def coin_change_problem(A, k):
    n = len(A)
    aux_tab = [0]*(k+1)
    for x in range(n):
        aux_tab[A[x]] = 1
    for x in range(A[0], k+1):
        ctr = inf
        for y in range(len(A)):
            if x >= A[y]:
                ctr = min(ctr, aux_tab[x-A[y]])
        aux_tab[x] = ctr + 1
    return aux_tab


A = [1, 7, 9]
print(coin_change_problem(A, 14))

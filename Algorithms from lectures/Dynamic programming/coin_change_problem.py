# Problem wydawania reszty polega na wydaniu określonej kwoty jak najmniejszą ilością monet, jednakże za każdym razem
# dostępne nominały mogą być inne (zawsze podane na początku zadania). Ilość monet określonego nominału jest
# nieograniczona.
# f(i, j) - minimalna ilość monet potrzebnych do wydania kwoty j posiadająć i pierwszych monet
# f(i, j) = min(f(i-1), j), f(i-1, j-A[i]) - albo daną monetę o określonym nominale weźmiemy, albo nie
# f(0, j) = inf
# f(1, j) = 1 if i is in A
# W przypadku rekurencji ze spamiętywaniem nie trzeba robić zagnieżdżonych funkcji, ponieważ modyfikujemy tablicę,
# która i tak jest przekazywana przez referencję. Jeśli chcelibyśmy modyfikować zmienną przekazywaną przez wartość,
# to wtedy wydaje mi się że zabieg jest konieczny z zagnieżdżonymi funkcjami i zmienną nonlocal.
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
    return aux_tab[k]


def coin_change_problem_memoized(tab, k):
    def reku(tab, n):
        nonlocal aux_tab
        xd = inf
        if aux_tab[n] != inf:
            return aux_tab[n]
        for x in range(len(tab)):
            if n - tab[x] >= 0:
                xd = min(xd, reku(tab, n-tab[x])+1)
        aux_tab[n] = xd
        return aux_tab[n]

    n = len(tab)
    aux_tab = [inf]*(k+1)
    for x in range(n):
        aux_tab[tab[x]] = 1
    aux_tab[0] = 0
    reku(tab, k)
    return aux_tab[k]


tab = [1, 2, 5]
k = 33
print(coin_change_problem(tab, k))

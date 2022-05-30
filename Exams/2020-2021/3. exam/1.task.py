# Passed all tests - last one 28 s!
# Done with O(n^2)

from zad1testy import runtests


def strictly_decreasing(X):
    for x in range(len(X) - 1):
        if X[x] >= X[x + 1]:
            return False
    return True


def strictly_increasing(X):
    for x in range(len(X) - 1):
        if X[x] <= X[x + 1]:
            return False
    return True


def lcs(X):
    n = len(X)
    lcs_tab = [1] * n
    lcs_parent = [-1] * n
    for x in range(n - 1, -1, -1):
        best = 0
        for y in range(x + 1, n):
            if X[y] > X[x] and best < lcs_tab[y]:
                best = lcs_tab[y]
                lcs_parent[x] = y
        lcs_tab[x] = best + 1
    return lcs_tab, lcs_parent


def lds(X):
    n = len(X)
    lds_tab = [1] * n
    lds_parent = [-1] * n
    for x in range(1, n):
        best = 0
        for y in range(x):
            if X[y] > X[x] and best < lds_tab[y]:
                best = lds_tab[y]
                lds_parent[x] = y
        lds_tab[x] = best + 1
    return lds_tab, lds_parent


def find_index(lds_tab, lcs_tab):
    index = 0
    for x in range(len(lds_tab)):
        if lds_tab[x] + lcs_tab[x] > lds_tab[index] + lcs_tab[index]:
            index = x
    return index


def find_solution(X, lds_parent, lcs_parent, index):
    solution = []
    t = index
    while t != -1:
        solution.append(X[t])
        t = lds_parent[t]
    t = index
    solution = solution[::-1]
    while lcs_parent[t] != -1:
        t = lcs_parent[t]
        solution.append(X[t])
    return solution


def mr(X):
    if strictly_increasing(X) or strictly_decreasing(X):
        return X
    lcs_tab, lcs_parent = lcs(X)
    lds_tab, lds_parent = lds(X)
    index = find_index(lds_tab, lcs_tab)
    return find_solution(X, lds_parent, lcs_parent, index)


runtests(mr)
# X = [4, 10, 5, 1, 2, 3, 4]
#
# print(mr(X))

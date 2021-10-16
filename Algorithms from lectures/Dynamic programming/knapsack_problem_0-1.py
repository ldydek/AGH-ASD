# [ENG] In 0-1 knapsack problem is given a set of items and each item has its own value. Our goal is to take some of
# this items (possibly everything) and total value of them is as large as possible, but there is one condition
# - we can't exceed given total weight of included items. 0-1 knapsack problem means that we don't have copies of
# same elements. Let's try dynamic programming approach to solve this problem.
# Function: f(i, j) - maximum value we can obtain taking items from tab[0] to tab[i] without exceeding weight "j"
# Basic cases: f(0, j) = P[0] (for "j" from W[0] to maximum possible weight)
# f(i, 0) = 0, because if we have weight equal to 0 we can't take anything
# Recursion: f(i, j) = max(f(i-1, j), f(i-1, j-W[i]) + P[i])
# Solution: aux_tab[n-1][max_w], where aux_tab is an array for keeping values of solved subproblems
# [PL] W 0-1 problemie plecakowym mamy dany zbiór przedmiotów, które możemy ze sobą zabrać. Dodatkowo każdy przedmiot
# ma wagę oraz cenę. Naszym celem jest wzięcie pewnej ilości przedmiotów tak, aby ich łączna cena była możliwie jak
# największa oraz ich waga nie przekraczała zadanego limitu. Problem spróbujemy rozwiązać za pomocą programowania
# dynamicznego. 0-1 problem plecakowy oznacza, że nie dopuszczamy kopiowania tych samym elementów (jeśli dany przedmiot
# bierzemy, to możemy to uczynić tylko jeden raz).
from math import inf


def bottom_up_knapsack_problem(W, P, max_w):
    n = len(W)
    aux_tab = [[0 for _ in range(max_w+1)] for _ in range(n)]
    for x in range(W[0], max_w+1):
        aux_tab[0][x] = P[0]
    for x in range(1, n):
        for y in range(1, max_w+1):
            aux_tab[x][y] = aux_tab[x-1][y]
            if y >= W[x]:
                aux_tab[x][y] = max(aux_tab[x][y], aux_tab[x-1][y-W[x]]+P[x])
    return aux_tab[n-1][max_w]


def top_down_knapsack_problem(W, P, max_w):
    n = len(W)
    aux_tab = [[inf for _ in range(max_w+1)] for _ in range(n)]
    for x in range(n):
        aux_tab[x][0] = 0
    for x in range(W[0], max_w+1):
        aux_tab[0][x] = P[0]
    for x in range(W[0]):
        aux_tab[0][x] = 0
    # [ENG] Basic cases
    # [PL] Warunki brzegowe
    recursion(aux_tab, W, P, n-1, max_w)
    return aux_tab[n-1][max_w]


def recursion(aux_tab, W, P, n, max_w):
    if aux_tab[n][max_w] != inf:
        return aux_tab[n][max_w]
    aux_tab[n][max_w] = recursion(aux_tab, W, P, n-1, max_w)
    if max_w >= W[n]:
        aux_tab[n][max_w] = max(aux_tab[n][max_w], recursion(aux_tab, W, P, n-1, max_w - W[n]) + P[n])
    return aux_tab[n][max_w]


P = [5, 7, 8, 34, 130]
W = [2, 5, 7, 10, 40]
print(bottom_up_knapsack_problem(W, P, 50))
print(top_down_knapsack_problem(W, P, 50))

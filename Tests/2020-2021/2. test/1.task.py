# Dynamic programming solution.
# f(i, j) - maximum quantity of students, that can live in student houses considering the set {A[0],...,A[i]}
# without exceeding price "j"
# either we given house include in our solution or not, so recursion is as follows:
# f(i, j) = max(f(i-1, j), f(prev(i), j-price(i))+student(i))
# prev(i) - first house on the left from considered, which not intersects (not necessarily it is A[i-1]!)
# price(i) - price of building "i" house
# student(i) - number of students who can live in "i" house
# task in some way similar to knapsack problem
# Time complexity: O(np + n log n)
# Space complexity: O(np)
# Passed all tests
from math import inf


def choose(tab, k):
    index = False
    diff = inf
    for x in range(len(tab)):
        if k[1] - tab[x][2] <= diff and k[1] > tab[x][2]:
            diff = k[1] - tab[x][2]
            index = x
    return index


def show_previous(T, prev):
    for x in range(len(T)):
        T[x] = (T[x][0], T[x][1], T[x][2], T[x][3], x)
    T.sort(key=lambda x: x[2])
    for x in range(len(T)):
        sol = choose(T, T[x])
        if sol is not False:
            prev[x] = sol


def students(x):
    return (x[2]-x[1])*x[0]


def select_buildings(T, p):
    n = len(T)
    prev = [-1] * n
    show_previous(T, prev)
    aux_tab = [[0 for _ in range(p)] for _ in range(n)]
    for x in range(T[0][3], p):
        aux_tab[0][x] = students(T[0])
    for x in range(1, n):
        for y in range(p):
            aux_tab[x][y] = aux_tab[x-1][y]
            if y >= T[x][3]:
                if prev[x] != -1:
                    aux_tab[x][y] = max(aux_tab[x][y], aux_tab[prev[x]][y-T[x][3]]+students(T[x]))
                else:
                    aux_tab[x][y] = max(aux_tab[x][y], students(T[x]))
    return aux_tab[n-1][p-1]


def print_solution(T, aux_tab, p, prev):
    n = len(aux_tab)
    solution = []
    k = n-1
    while k != 0 and k != -1:
        if aux_tab[k][p] != aux_tab[k-1][p]:
            solution.append(T[k][4])
            p -= T[k][3]
            k = prev[k]
        else:
            k -= 1
    if k == 0:
        if p >= T[0][3]:
            solution.append(T[0][4])
    solution.sort()
    return solution


T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
p = 6
print(select_buildings(T, p))

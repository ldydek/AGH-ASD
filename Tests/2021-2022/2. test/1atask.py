# Dynamic programming approach
# f(v) - minimum amount of control points visited by Marian when Jacek is driving to "v" change point
# g(v) - minimum amount of control points visited by Marian when Marian is driving to "v" change point
# recursion:
# f(v) = min(g(v-1), g(v-2), g(v-3))
# g(v) = min(f(v-1)+cost(i-1,i), f(v-2)+cost(i-2,i), f(v-3)+cost(i-3,i))
# cost function defines number of control points between given two change points as arguments
# basic cases:
# g(1) = 0 - thanks to it we can now start computing values starting from Jacek (he is driving at the beginning)
# Before using dynamic programming we have to sort given list. In an auxiliary array we can keep information about how
# many control points are from the beginning. Thanks to it we can read in constant time how many control points are
# between certain two change points. Additionally, we can treat final destination as last change point.
# Time complexity: O(n log n)
# Space complexity: O(n)
# Passed all tests
# Time for all tests: ~ 0.04s

from kol2atesty import runtests
from math import inf


def cost(P, x, y):
    return P[y] - P[x]


def drivers(P, B):
    P.append((B, True))
    n = len(P)
    for x in range(n):
        P[x] = (P[x][0], P[x][1], x)
    P.sort()
    p_points = [0]
    ctr = 0
    for x in range(n):
        if P[x][1] is False:
            ctr += 1
        else:
            p_points.append(ctr)
    if ctr not in p_points:
        p_points.append(ctr)
    n = len(p_points)
    dp = [[inf for _ in range(n)] for _ in range(2)]
    parent = [[(-1, -1) for _ in range(n)] for _ in range(2)]
    dp[1][0] = 0
    for x in range(1, n):
        value1, value2 = inf, inf
        for y in range(1, 4):
            if x < y:
                continue
            if value1 > dp[1][x-y]:
                value1 = dp[1][x-y]
                parent[0][x] = (1, x-y)
            if value2 > dp[0][x-y] + cost(p_points, x-y, x):
                value2 = dp[0][x-y] + cost(p_points, x-y, x)
                parent[1][x] = (0, x-y)
        dp[0][x] = value1
        dp[1][x] = value2
    index = choose_driver(dp)
    p_points_ids = [0]
    for x in range(len(P)):
        if P[x][1] is True:
            p_points_ids.append(P[x][2])
    return print_solution(parent, index, p_points_ids)
    # return dp


def choose_driver(dp):
    n = len(dp[0])
    index = 0
    if dp[index][n-1] > dp[1][n-1]:
        index = 1
    return index


def print_solution(parent, index, p_points_ids):
    solution = []
    a, b = index, len(parent[0])-1
    a, b = parent[a][b]
    while parent[a][b] != (-1, -1):
        solution.append(p_points_ids[b])
        a, b = parent[a][b]
    return solution[::-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(drivers, all_tests=True)

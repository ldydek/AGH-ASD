# We can travel between remote car parks only once, so idea is to firstly compute cheapest path to get to "i" car park
# without using this special ability to travel to remote car parks. In one array we store these information to get to
# "i" car park from starting position and in the second one to get from "i" car park to the final destination. At the
# end, we have to determine between which car parks we can use this special ability, so we have to choose certain "i"
# and "j" indexes from the array for which path from starting to final place is truly the cheapest.
# Time complexity: O(n^2)
# Space complexity: O(n)
# Passed all tests
# Time for all tests: ~ 652s ;(

from kol2btesty import runtests


def distance(O, x, y):
    return O[y][0] - O[x][0]


def fill_f(O, f, T):
    n = len(f)
    for x in range(1, n):
        value = float("inf")
        for y in range(x):
            if distance(O, y, x) <= T:
                value = min(value, f[y])
        f[x] = value + O[x][1]


def fill_g(O, g, T):
    n = len(g)
    for x in range(n-2, -1, -1):
        value = float("inf")
        for y in range(x+1, n):
            if distance(O, x, y) <= T:
                value = min(value, g[y])
        g[x] = value + O[x][1]


def get_solution(O, f, g, T):
    n = len(O)
    solution = float("inf")
    for x in range(n):
        for y in range(n):
            if T < distance(O, x, y) <= 2 * T:
                solution = min(solution, f[x] + g[y])
    return solution


def min_cost(O, C, T, L):
    O.append(0)
    O.append(L)
    C.append(0)
    C.append(0)
    n = len(O)
    for x in range(n):
        O[x] = (O[x], C[x])
    O.sort()
    f = [float("inf")] * n
    g = [float("inf")] * n
    f[0] = 0
    g[-1] = 0
    fill_f(O, f, T)
    fill_g(O, g, T)
    return get_solution(O, f, g, T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)

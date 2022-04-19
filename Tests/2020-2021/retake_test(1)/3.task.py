# Dynamic programming approach
# f(i, j) - minimum quantity of petrol station that manager has to visit to get to "i-th" station and has "j" litres
# of fuel before fuel a vehicle
# recursion: f(i, j) = f(i-k, max(0, j+dist(i-k,i)-min(V[i-k],q)))
# - dist(i-k,i) - distance between (i-k)th and ith stations
# - min(V[i-k], q) - condition happens when one of the previous gas stations had more fuel than a tank in the vehicle
# - max(0, j+dist(i-k,i)-min(V[i-k],q)) - condition happens when one of the previous gas stations had more fuel than
# temporary amount of it in a vehicle tank (in other words amount of fuel can't be negative)
# solution: min(f(n-1, j) where 0 <= j <= q, where "q" is a capacity of vehicle tank and additional "parent" array
# that helps us construct the final solution
# Passed all tests
from math import inf


def distance(T, x, y):
    return T[y] - T[x]


def find_index(aux_tab, q):
    index = None
    value = inf
    n = len(aux_tab)
    for x in range(q+1):
        if aux_tab[n-1][x] < value:
            value = aux_tab[n-1][x]
            index = x
    return index


def iamlate(T, V, q, l):
    T.append(l)
    V.append(0)
    n = len(T)
    aux_tab = [[inf for _ in range(q+1)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(q+1)] for _ in range(n)]
    aux_tab[0][0] = 0
    for x in range(1, n):
        for y in range(q+1):
            best = inf
            ctr = x-1
            while ctr >= 0 and y + distance(T, ctr, x) <= q:
                if best > aux_tab[ctr][max(0, y+distance(T, ctr, x)-min(V[ctr], q))]:
                    best = aux_tab[ctr][max(0, y+distance(T, ctr, x)-min(V[ctr], q))]
                    parent[x][y] = (ctr, max(0, y+distance(T, ctr, x)-min(V[ctr], q)))
                ctr -= 1
            aux_tab[x][y] = best + 1
    index = find_index(aux_tab, q)
    if index is None:
        return []
    return print_solution(parent, n-1, index)


def print_solution(parent, x, y):
    solution = []
    while parent[x][y] != (-1, -1):
        solution.append(parent[x][y][0])
        x, y = parent[x][y]
    return solution[::-1]


T = [0, 1, 2]
V = [2, 1, 5]
q = 2
l = 4
print(iamlate(T, V, q, l))

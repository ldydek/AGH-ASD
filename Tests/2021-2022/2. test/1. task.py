# Lukasz Dydek
# Podejście dynamiczne
# g(i) - minimalna ilość punktów kontrolnych minięta przez Mariana do "i-tego" punktu przesiadkowego, kiedy dojeżdża
# do niego Jacek
# f(i) - to samo co wyżej ale Marian kieruje
# rekursja:
# f(i) = min(g(i-1) + dist(i-1,i), g(i-2) + dist(i-2,i), g(i-3) + dist(i-3, i))
# g(i) = min(f(i-1), f(i-2), f(i-3))
# dist(i-1,i) - odlegosc pomiedzy "i-1-wszym" a"i-tym" punktem przesiadkowym
# W tablicy dp pierwszy wiersz to wartosci funkcji f a drugi g

from kol2atesty import runtests


def drivers(P, B):
    n = len(P)
    points = [0] * (n+1)
    points[0] = 1
    c_points = []
    p_points = []
    for x in range(n):
        if P[x][1] is False:
            c_points.append(P[x][0])
        elif P[x][1] is True:
            p_points.append(P[x][0])
    for x in range(n):
        if P[x][1] is True:
            points[P[x][0]] = 1
    dp = [[10**10 for _ in range(len(p_points))] for _ in range(2)]
    distances = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        ctr = 0
        if points[x] == 1:
            for y in range(x+1, n):
                if points[y] == 0:
                    ctr += 1
                else:
                    distances[x][y] = ctr
    # 0 - Marian
    # 1 - Jacek
    dp[0][0] = dp[1][0] = 0
    for x in range(1, len(p_points)):
        best = 10**10
        for y in range(1, 4):
            if x >= y:
                best = min(best, dp[0][x-y] + distances[p_points[x-y]][p_points[x]])
                dp[1][x] = min(dp[1][x], dp[0][x-y])
        dp[0][x] = best
    return dp


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(drivers, all_tests=False)
c = False
p = True
P = [(1, c), (3, c), (4, c), (6, c), (8, c), (9, c), (11, c), (13, c), (16, c), (17, c),
         (2, p), (5, p), (7, p), (10, p), (12, p), (14, p), (15, p), (18, p)]
B = []
print(drivers(P, B))
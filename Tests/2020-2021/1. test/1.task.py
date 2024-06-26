# At the beginning, with the use of "quick_select" function in O(n^2) I check, which numbers would be in the upper right
# and bottom left corners after sorting entire matrix. Later, I create proper main diagonal adding elements on their 
# appropriate places. At the end, I iterate through two halves (main diagonal divides them) and if values are not
# suitable I am forced to swap these elements.
# Time complexity: O(n^2)
# Space complexity: O(1)
# Passed tests


def partition(tab, p, r):
    p = (p//len(tab), p % len(tab))
    r = (r//len(tab), r % len(tab))
    x = tab[r[0]][r[1]]
    i = (p[0], p[1]-1)
    j = p
    while j != r:
        if tab[j[0]][j[1]] <= x:
            i = (i[0], i[1]+1)
            if i[1] >= len(tab):
                i = (i[0] + 1, 0)
            tab[i[0]][i[1]], tab[j[0]][j[1]] = tab[j[0]][j[1]], tab[i[0]][i[1]]
        j = (j[0], j[1]+1)
        if j[1] >= len(tab):
            j = (j[0]+1, 0)
    i = (i[0], i[1]+1)
    if i[1] >= len(tab):
        i = (i[0] + 1, 0)
    tab[i[0]][i[1]], tab[r[0]][r[1]] = tab[r[0]][r[1]], tab[i[0]][i[1]]
    return i[0] * len(tab) + i[1]


def quick_select(tab, p, r, i):
    if p == r:
        return tab[p//len(tab)][p%len(tab)]
    q = partition(tab, p, r)
    k = q - p + 1
    if k == i:
        return tab[q//len(tab)][q%len(tab)]
    elif k < i:
        return quick_select(tab, q+1, r, i-k)
    else:
        return quick_select(tab, p, q-1, i)


def seeking(tab, c, d):
    n = len(tab)
    a = b = None
    for x in range(n):
        for y in range(n):
            if tab[x][y] == c:
                a = (x, y)
            if tab[x][y] == d:
                b = (x, y)
    return a, b


def Median(T):
    n = len(T)
    a = len(T) * len(T) // 2 - len(T) // 2 + 1
    if len(T) % 2:
        b = len(T) * len(T) // 2 + len(T) // 2 + 1
    else:
        b = len(T) * len(T) // 2 + len(T) // 2
    c = quick_select(T, 0, len(T)*len(T)-1, a)
    d = quick_select(T, 0, len(T)*len(T)-1, b)
    c, d = seeking(T, c, d)
    T[0][0], T[c[0]][c[1]] = T[c[0]][c[1]], T[0][0]
    T[n-1][n-1], T[d[0]][d[1]] = T[d[0]][d[1]], T[n-1][n-1]
    c, d = 1, 1
    for x in range(n):
        for y in range(n):
            if T[0][0] < T[x][y] < T[n-1][n-1]:
                T[c][d], T[x][y] = T[x][y], T[c][d]
                c += 1
                d += 1
    a = (0, 1)
    b = (1, 0)
    while a != (n-2, n-1) and b != (n-1, n-2):
        while T[a[0]][a[1]] > T[n-1][n-1] and T[b[0]][b[1]] < T[0][0]:
            a = (a[0], a[1]+1)
            if a[1] == n:
                a = (a[0]+1, a[0]+2)
            b = (b[0], b[1]+1)
            if b[1] == b[0]:
                b = (b[0]+1, 0)
        while T[a[0]][a[1]] > T[n-1][n-1]:
            a = (a[0], a[1] + 1)
            if a[1] == n:
                a = (a[0] + 1, a[0] + 2)
        while T[b[0]][b[1]] < T[0][0]:
            b = (b[0], b[1] + 1)
            if b[0] == b[1]:
                b = (b[0]+1, 0)
        T[a[0]][a[1]], T[b[0]][b[1]] = T[b[0]][b[1]], T[a[0]][a[1]]
    if T[a[0]][a[1]] < T[b[0]][b[1]]:
        T[a[0]][a[1]], T[b[0]][b[1]] = T[b[0]][b[1]], T[a[0]][a[1]]
    return T


tab = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
print(Median(tab))

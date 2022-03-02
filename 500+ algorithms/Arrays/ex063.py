# O(n log n) - sorting
def ex063a(tab):
    n = len(tab)
    tab.sort()
    solution = []
    k = n // 2 - 1
    while k:
        tab[k] = (tab[k][1], tab[k][0])
        k -= 1
    tab.sort()
    for x in range(1, n):
        if tab[x-1] == tab[x]:
            solution.append(tab[x])
            tab[x] = (tab[x][1], tab[x][0])
            solution.append(tab[x])
    return solution


# O(n) - hashing
def ex063b(tab):
    n = len(tab)
    s = set()
    solution = []
    for x, y in tab:
        s.add((x, y))
        if (y, x) in s:
            solution += [(x, y), (y, x)]
    return solution


tab = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
print(ex063a(tab))

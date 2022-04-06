def ex015(tab):
    n = len(tab)
    aux_tab = [0] * n
    parent = [-1] * n
    for x in range(n):
        aux_tab[x] = tab[x]
    for x in range(1, n):
        maxi = 0
        for y in range(x):
            if tab[x] > tab[y]:
                if aux_tab[y] > maxi:
                    maxi = aux_tab[y]
                    parent[x] = y
        aux_tab[x] = maxi + tab[x]
    maxi, max_index = 0, 0
    for x in range(n):
        if aux_tab[x] > maxi:
            maxi = aux_tab[x]
            max_index = x
    return print_solution(parent, tab, max_index)


def print_solution(parent, tab, x):
    solution = []
    while x != -1:
        solution.append(tab[x])
        x = parent[x]
    return solution[::-1]


tab = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
print(ex015(tab))

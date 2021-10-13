# Najdłuższy rosnący podciąg znajdowany za pomocą programowania dynamicznego.
# f(i) - najdłuższy rosnący podciąg składający się z elementów na indeksach tablicy od 0 do i
# f(0) = 1
# f(i) = max(f(k)) + 1, gdzie k jest pewnym indeksem wcześniej, a więc f(k) będzie długością najdłuższego podciągu
# od 0 do k

def lis(tab):
    n = len(tab)
    aux_tab = [1]*n
    parent = [-1]*n
    for x in range(1, n):
        ctr1, ctr2 = 0, 0
        for y in range(x):
            if tab[y] < tab[x]:
                if aux_tab[y] > ctr1:
                    ctr1 = aux_tab[y]
                    ctr2 = y
        aux_tab[x] = ctr1 + 1
        parent[x] = ctr2

    ctr, ctr1 = 0, 0
    for x in range(n):
        if aux_tab[x] > ctr:
            ctr = aux_tab[x]
            ctr1 = x
    return print_solution(parent, ctr1)


def print_solution(parent, x):
    set1 = [tab[x]]
    while parent[x] != -1:
        set1.append(tab[parent[x]])
        x = parent[x]
    if set1[len(set1)-2] < set1[len(set1)-1]:
        del set1[len(set1)-1]
    return set1[::-1]


tab = [1, 40, 2, 5, 7, 2, 4, 9, 3, 17, 3]
print(lis(tab))

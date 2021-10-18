# [ENG] In some problems grouping "n" distinct elements into a collection of disjoint sets will help solve them.
# Structure of disjoint sets enables following operations:
# - make-set(x) - creates new set whose only member is "x"
# - union(x, y) - unites two sets with "x" and "y"
# - find-set(x) - shows us set representative of set containing "x"
# If we use union by rank (joining tree with less height to the second one) and path compression (looking for a
# representative during recursive returns we update a pointer to the representative in visited elements) and represent
# sets as rooted trees we can significantly improve time complexity to almost linear regarding to all operations.
# [PL] W niektórych problemach grupowanie "n" parami różnych elementów w rodzinę rozłącznych podzbiorów może pomóc
# w ich rozwiązaniu. Struktura zbiorów rozłącznych umożliwia poniższe operacje:
# - make-set(x) - stwórz nowy zbiór, którego jedynym elementem jest "x"
# - union(x, y) - złącz dwa rozłączne zbiory zawierające "x" i "y"
# - find-set(x) - zwróć reprezentanta zbioru zawierającego "x"
# Jeśli użyjemy łączenia wg rangi (dołączanie drzewa o mniejszej wysokości do tego o większej) oraz kompresji ścieżki
# (szukając reprezentanta, podczas powrotów rekurencyjnych uaktualniamy wskaźnik bezpośrednio na niego w odwiedzonych
# elementach), a zbiory zaprezentujemy jako drzewa ukorzenione znacząco możemy polepszyć złożoność czasową do
# praktycznie liniowej względem ilości wszystkich operacji.
from math import inf


def make_set(tab):
    n = len(tab)
    v = -inf
    for x in range(n):
        v = max(v, tab[x][0], tab[x][1])
    return v


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1


def find_union_make_set(tab):
    v = make_set(tab)
    v += 1
    n = len(tab)
    parent = [x for x in range(v)]
    rank = [0]*v
    for x in range(n):
        if find(parent, tab[x][0]) != find(parent, tab[x][1]):
            union(tab[x][0], tab[x][1], parent, rank)
    return parent


tab = [(0, 1), (1, 4), (1, 2), (2, 3), (5, 6), (3, 5)]
print(find_union_make_set(tab))


def surface_area(x):
    return (x[1] - x[3]) * (x[2] - x[0])


def partition(tab, p, r, index):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j][index] <= x[index]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[r], tab[i+1] = tab[i+1], tab[r]
    return i+1


def quicksort(tab, p, r, index):
    while p < r:
        q = partition(tab, p, r, index)
        quicksort(tab, p, q-1, index)
        p = q + 1
    return tab


def ex04(vessels, A):
    n = len(vessels)
    for x in range(n):
        vessels[x] = (vessels[x][0], vessels[x][1], vessels[x][2], vessels[x][3], surface_area(vessels[x]))
    quicksort(vessels, 0, len(vessels)-1, 4)
    quicksort(vessels, 0, len(vessels)-1, 1)
    ctr, water = -1, 0
    while ctr < n - 1 and water < A:
        ctr += 1
        water += vessels[ctr][4]
    if water <= A:
        ctr += 1
    return ctr


vessels = [(0, 1, 1, 0), (2, 2, 3, 1), (4, 1, 6, 0), (1, 5, 4, 3)]
print(ex04(vessels, 17))

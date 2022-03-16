def surface_area(x):
    return (x[0][1] - x[1][1]) * (x[1][0] - x[0][0])


def ex04(vessels, A):
    n = len(vessels)
    for x in range(n):
        vessels[x] = (vessels[x][0], vessels[x][1], surface_area(vessels[x]))
    vessels = sorted(vessels, key=lambda x: x[2])
    vessels = sorted(vessels, key=lambda x: x[0][1])
    ctr, water = -1, 0
    while ctr < n - 1 and water < A:
        ctr += 1
        water += vessels[ctr][2]
    if water <= A:
        ctr += 1
    return ctr


vessels = [((0, 1), (1, 0)), ((2, 2), (3, 1)), ((4, 1), (6, 0)), ((1, 5), (4, 3))]
print(ex04(vessels, 2))

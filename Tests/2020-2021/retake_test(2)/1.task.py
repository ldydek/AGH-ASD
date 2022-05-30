# Idea bases on prefix sum method. We allocate two additional arrays and store on "i" vertex intersection of "i-1" first
# rectangles in the first one and "i-1" last in the second one. Now we can compute intersection of all rectangles apart
# from, for instance, second one taking second indexes from both arrays. We chose this vertex for which intersection
# of all remaining rectangles generates the biggest surface area.
# Time complexity: O(n)
# Space complexity: O(n)
# Passed all tests
from math import inf


# function computing intersection of two rectangles
def intersection(a, b):
    # if one of them is a whole surface simply return second one
    if a == (inf, inf, inf, inf):
        return b
    elif b == (inf, inf, inf, inf):
        return a
    # if these rectangles don't intersect
    elif (a[2] < b[0] and a[3] < b[1]) or (b[2] < a[0] and b[3] < a[1]):
        return 0, 0, 0, 0
    # basic case
    return max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])


# function computing surface area of an intersection (which is also a rectangle)
def surface(a):
    return (a[2] - a[0]) * (a[3] - a[1])


# main function with a prefix sum idea
def rect(D):
    n = len(D)
    intersection1 = [(inf, inf, inf, inf) for _ in range(n)]
    intersection2 = [(inf, inf, inf, inf) for _ in range(n)]

    for x in range(1, n):
        intersection1[x] = intersection(intersection1[x-1], D[x-1])
    for x in range(n-2, -1, -1):
        intersection2[x] = intersection(intersection2[x+1], D[x+1])
    index, value = None, -inf
    for x in range(n):
        if surface(intersection(intersection1[x], intersection2[x])) > value:
            value = surface(intersection(intersection1[x], intersection2[x]))
            index = x
    return index


D = [(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7), (1, 1, 2, 2)]
print(rect(D))


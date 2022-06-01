# Firstly, we remember with each tuple its index in a given array. Later, we sort tuples using, for instance, quicksort.
# Tuple (2, 5) > (1, 6) and tuple (1, 2) > (1, 1)! Now we can add to the solution array index of the first element,
# because it will be always included. Now we traverse sorted array and look for next point which is not dominated by
# last element in  a solution array (at the beginning it will be first element index of a sorted points array
# of course). When we traverse  entire array we found all points indexes that were necessary. At the end, we can change
# points indexes to the indexes from the input array before sorting (thanks to third element in a tuple).
# Time complexity: O(n log n)
# Space complexity: O(n)
# Passed all tests


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[r], tab[i+1] = tab[i+1], tab[r]
    return i + 1


# quicksort algorithm with partition implementation
def quick_sort(P, p, r):
    while p < r:
        q = partition(P, p, r)
        p = q + 1


# function checking whether point "x" dominates point "y"
def if_dominance(x, y):
    if x[0] <= y[0] and x[1] <= y[1]:
        return True
    return False


def dominance(P):
    n = len(P)
    for x in range(n):
        P[x] = (P[x][0], P[x][1], x)
    quick_sort(P, 0, n-1)
    solution = [0]
    for x in range(1, n):
        if if_dominance(P[solution[-1]], P[x]) is False:
            solution.append(x)
    for x in range(len(solution)):
        solution[x] = P[solution[x]][2]
    return solution


P = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]
print(dominance(P))

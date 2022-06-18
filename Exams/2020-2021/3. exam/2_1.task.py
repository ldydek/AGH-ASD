# Firstly, we sort entire list. Later, for each pair of strings we check how many first letters they have in common.
# We write them in an auxiliary array. After this we can have a situation when one nice string is a prefix of another
# nice string, so it is not very nice. To remove only nice strings we can sort nice strings array and search for this
# string for which it is not a prefix of next one. All these strings are very nice.
# Time complexity: O(dn log n)
# Space complexity: O(dn)
# Passed all tests

# O(d) - function checking whether string "a" is a prefix of string "b"
def prefix(a, b):
    for x in range(len(a)):
        if a[x] != b[x]:
            return False
    return True


# O(dn log n + dn) = O(dn log n) - function checking which strings are only
# nice and rewriting very nice ones to another array with a solution
def removing_prefixes(tab):
    n = len(tab)
    tab.sort()
    taken = [0] * n
    for x in range(1, n):
        if prefix(tab[x-1], tab[x]) is False:
            taken[x-1] = 1
    taken[n-1] = 1
    solution = []
    for x in range(n):
        if taken[x] == 1:
            solution.append(tab[x])
    return solution


# O(2 * dn log n) = O(dn log n)
def double_prefix(L):
    n, ctr = len(L), 0
    L.sort()
    tab = [[]]
    for x in range(1, n):
        for y in range(len(L[x-1])):
            if L[x-1][y] != L[x][y]:
                break
            tab[ctr].append(L[x-1][y])
        if len(tab[ctr]) > 0:
            tab[ctr] = ''.join(tab[ctr])
            ctr += 1
            tab.append([])
    tab.pop()
    return removing_prefixes(tab)


L = ['00111', '0010001', '00001', '0101111', '0001000', '0100010', '001011', '0010010']
print(double_prefix(L))

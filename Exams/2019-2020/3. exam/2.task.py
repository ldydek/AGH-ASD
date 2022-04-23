# f(i) - minimal height we can obtain considering "i" first bricks and including "i-th" brick to the solution
# recursion: f(i) = max(f(k)) + 1, where 0 <= k <= i-1 and A[k] can contain A[i]
# solution: max(f(i)), where 0 <= i <= n-1 ("n" is the number of bricks)
# Passed all tests

def include(x, y):
    return x[0] <= y[0] and y[1] <= x[1]


def tower(A):
    n = len(A)
    aux_tab = [1] * n
    for x in range(1, n):
        best = 0
        for y in range(x):
            if include(A[y], A[x]):
                best = max(best, aux_tab[y])
        aux_tab[x] = best + 1
    return max(aux_tab)


A = [(1, 4), (0, 6), (1, 5), (2, 4), (2, 4), (2, 3)]
print(tower(A))

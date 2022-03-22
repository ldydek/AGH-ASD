# In-place merging two sorted arrays.
# Time complexity: O(mn) where "m" and "n" are sizes of these two arrays.

def move_element(tab):
    n = len(tab)
    x = tab[0]
    for i in range(1, n):
        if x < tab[i]:
            return tab
        tab[i-1] = tab[i]
        tab[i] = x
    tab[n-1] = x
    return tab


def ex035(X, Y):
    n = len(X)
    for a in range(n):
        if X[a] > Y[0]:
            X[a], Y[0] = Y[0], X[a]
            move_element(Y)
    return X


X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]
print(ex035(X, Y))

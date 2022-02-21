# [ENG] This time I slightly modify binary search. If I find an appropriate number I move to the left and continue
# searching in that part of an array.
# Time complexity: O(lg n)
# [PL] Tym razem lekko modyfikuję wyszukiwanie binarne. Jeżeli znajdę szukaną liczbę kontynuuję wyszukiwanie binarne
# w tablicy, poruszając się w lewo.
# Złożoność czasowa: O(lg n)


def ex06(tab, k):
    n = len(tab)
    l, r = 0, n - 1
    solution = False
    while l <= r:
        m = (l + r) // 2
        if tab[m] == k:
            solution = m
            r = m - 1
        elif tab[m] > k:
            r = m - 1
        else:
            l = m + 1
    return solution


tab = [1, 2, 2, 3, 3, 6, 7, 9, 10]
print(ex06(tab, 3))

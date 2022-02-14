# Algorytm wyszukiwania binarnego w tablicy. Uwaga! W podanej tablicy musi być zachowany porządek inaczej nie będziemy
# w stanie zlokalizować danego elementu szybciej niż przejście liniowe po całej tablicy.
# Złożność czasowa: O(lg n)
# Złożność pamięciowa: iteracyjnie - O(1), rekurencyjnie - O(lg n) w powodu odkładania funkcji rekurencyjnych na
# stosie.


def binary_search(tab, k):
    n = len(tab)
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if tab[m] == k:
            return m
        elif tab[m] > k:
            r = m - 1
        else:
            l = m + 1
    return False


tab = [2, 4, 6, 8, 9, 11, 14, 16]
print(binary_search(tab, 6))

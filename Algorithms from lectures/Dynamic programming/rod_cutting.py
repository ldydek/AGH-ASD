# [ENG] In rod cutting problem we get a rod of length "n" and we want to sell that rod in pieces and get as much
# money as possible knowing prices of various lengths of the rod. This problem exhibits optimal substructure, so we can
# try to find fast algorithm using dynamic programming.
# Function: f(i) - maximum profit we can get by selling rod of length "i"
# Basic case: f(0) = 0 (if length of the rod is 0 we can't sell anything)
# Recursion: f(i) = max(f(i-k) + tab[k]) for certain "k" (tab[k] is a profit of selling rod length "k")
# "k" is from 1 to "i".
# Time complexity: O(n^2)
# Space complexity: O(n) - extra space without considering data, which program gets at the input
# [PL] W problemie cięcia pręta, znając ceny za długości poszczegolnych prętów, tak musimy go pociąć, aby otrzymać
# z jego sprzedaży możliwie największy zysk. Dopuszczamy również możliwość sprzedaży pręta w całości. Problem ten
# charakteryzuje się optymalną podstrukturą, a więc dobrym pomysłem będzie użycie w jego rozwiązaniu programowania
# dynamicznego.
# Złożoność obliczeniowa: O(n^2)
# Złożoność pamięciowa: O(n) - pamięć dodatkowa, nie uwzględniając danych, które program przyjmuje na wejściu
from math import inf


def bottom_up_rod_cutting(prices):
    n = len(prices)
    aux_tab = [0]*n
    for x in range(1, n):
        q = -inf
        for y in range(1, x+1):
            q = max(q, aux_tab[x-y]+prices[y])
        aux_tab[x] = q
    return aux_tab[n-1]


# [ENG] We can easily modify function and get not only profit, but also best lengths of pieces after cutting
# [PL] Łatwo podaną funkcję można zmodyfikować, aby wyliczała nie tylko najlepszy zysk, ale również szukane długości

def bottom_up_rod_cutting_print_lengths(prices):
    n = len(prices)
    aux_tab = [0]*n
    parent = [-1]*n
    for x in range(1, n):
        q = -inf
        for y in range(1, x+1):
            if q < aux_tab[x-y]+prices[y]:
                q = aux_tab[x-y]+prices[y]
                parent[x] = x - y
        aux_tab[x] = q
    return print_path(parent, n-1), aux_tab[n-1]


def print_path(parent, x):
    solution = []
    while parent[x] != -1:
        solution.append(x-parent[x])
        x = parent[x]
    return solution[::-1]


# [ENG] Top-down approach to solve that problem.
# [PL] Rozwiązanie tego problemu za pomocą spamiętywania.

def top_down_rod_cutting(prices):
    def recursion(n, aux_tab):
        if aux_tab[n-1] != inf:
            return aux_tab[n-1]
        q = -inf
        for x in range(1, n):
            q = max(q, recursion(n-x, aux_tab)+prices[x])
        aux_tab[n-1] = q
        return q
    n = len(prices)
    aux_tab = [inf]*n
    aux_tab[0] = 0
    recursion(n, aux_tab)
    return aux_tab[n-1]

prices = [0, 1, 4, 50, 50]
print(bottom_up_rod_cutting_print_lengths(prices))

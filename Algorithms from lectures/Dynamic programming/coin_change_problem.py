# [ENG] In coin change problem we have known amount of money and our task is to find out what is the minimum number
# of coins that sum up to this amount. We know also given denominations at the beginning and there is unlimited number
# of this denominations. Dynamic programming is a good idea to solve this problem.
# Function: f(i) - minimum quantity of coins that we need to get the sum "i"
# Recursion: f(i) = min(f(i-tab[j]) + 1, where "tab" is an array of denominations, "j" is from 0 to length(tab)-1
# Basic cases: quantity of coins that we need to get amount of money equal to our denominations is 1
# Solution: aux_tab[k] where "aux_tab" is our array for keeping values of solved subproblems and "k" is our sum of
# money. Below is presented top-down and bottom-up approach to this problem.
# Time complexity: O(nk), where "k" is our sum of money and "n" number of denominations, so algorithm is
# pseudo-polynomial.
# Space complexity: O(k) - additional array in first approach or recursion call stack in the second one.
# [PL] W problemie wydawania reszty mamy podaną kwotę, którą należy wydać za pomocą dostępnych nominałów pieniędzy
# i należy to zrobić minimalną ilością monet. Nominały monet są znane na początku, a ich ilość jest nieograniczona.
# Programowanie dynaminczne jest dobrym pomysłem, aby ten problem rozwiązać.
# Złożoność czasowa: O(nk), gdzie "k" to kwota do wydania a "n" to ilość dostępnych nominałów, a więc algorytm jest
# pseudowielomianowy.
# Złożoność pamięciowa: O(k) - dodatkowa tablica w pierwszy podejściu czy rekurencyjne odkładanie funkcji na stosie
# w drugim.
# Poniżej zostało zaprezentowane podejście metodą wstępującą i zstępującą.
from math import inf


def bottom_up_coin_change_problem(tab, k):
    n = len(tab)
    aux_tab = [inf]*(k+1)
    parent = [-1]*(k+1)
    aux_tab[0] = 0
    b = min(tab)
    for x in range(n):
        if tab[x] <= k:
            aux_tab[tab[x]] = 1
#             [ENG] if denomination is bigger than our amount of money program will just ignore it
#             [PL]  jeśli nominał jest większy od naszej kwoty program po prostu go zignoruje
    for x in range(b, k+1):
        ctr = inf
        for y in range(n):
            if x >= tab[y] and ctr > aux_tab[x-tab[y]]:
                ctr = aux_tab[x-tab[y]]
                parent[x] = x - tab[y]
        aux_tab[x] = ctr + 1
    return print_coins(parent, k)


def top_down_coin_change_problem(tab, k):
    n = len(tab)
    aux_tab = [inf]*(k+1)
    parent = [-1]*(k+1)
    for x in range(n):
        if tab[x] <= k:
            aux_tab[tab[x]] = 1
            parent[tab[x]] = 0
    aux_tab[0] = 0
    recursion(tab, k, aux_tab, parent)
    return print_coins(parent, k)


def recursion(tab, n, aux_tab, parent):
    if aux_tab[n] != inf:
        return aux_tab[n]
    for x in range(len(tab)):
        if n - tab[x] >= 0:
            xd = recursion(tab, n-tab[x], aux_tab, parent)
            if xd + 1 < aux_tab[n]:
                aux_tab[n] = xd + 1
                parent[n] = n - tab[x]
    return aux_tab[n]


# [ENG] Additional function which shows us set of coins we took.
# [PL] Dodatkowa funkcja pokazująca nam, które monety zostały wzięte do rozwiązania.
def print_coins(parent, k):
    solution = []
    while parent[k] != -1:
        solution.append(k-parent[k])
        k = parent[k]
    return solution


tab = [3, 5, 7]
k = 39
print(top_down_coin_change_problem(tab, k))
print(bottom_up_coin_change_problem(tab, k))

# [ENG] In coin change problem we have known amount of money and our task is to find out what is the minimum number
# of coins that sum up to this amount. We know also given denominations at the beginning and there is unlimited number
# of this denominations. Dynamic programming is a good idea to solve this problem.
# Function: f(i) - minimum quantity of coins that we need to get the sum "i"
# Recursion: f(i) = min(f(i-tab[j]) + 1, where "tab" is an array of denominations, "j" is from 0 to length(tab)-1
# Basic cases: quantity of coins that we need to get amount of money equal to our denominations is 1
# Below is presented top-down and bottom-up approach to this problem.
# Time complexity: O(nk), where "k" is our sum of money and "n" number of denominations, so algorithm is
# pseudo-polynomial.
# [PL] W problemie wydawania reszty mamy podaną kwotę, którą należy wydać za pomocą dostępnych nominałów pieniędzy
# i należy to zrobić minimalną ilością monet. Nominały monet są znane na początku, a ich ilość jest nieograniczona.
# Programowanie dynaminczne jest dobrym pomysłem, aby ten problem rozwiązać.
# Złożoność czasowa: O(nk), gdzie "k" to kwota do wydania a "n" to ilość dostępnych nominałów, a więc algorytm jest
# pseudowielomianowy.
# Poniżej zostało zaprezentowane podejście metodą wstępującą i zstępującą.
from math import inf


def bottom_up_coin_change_problem(tab, k):
    n = len(tab)
    aux_tab = [0]*(k+1)
    for x in range(n):
        aux_tab[tab[x]] = 1
    for x in range(tab[0], k+1):
        ctr = inf
        for y in range(n):
            if x >= tab[y]:
                ctr = min(ctr, aux_tab[x-tab[y]])
        aux_tab[x] = ctr + 1
    return aux_tab


def top_down_coin_change_problem(tab, k):
    def reku(tab, n, aux_tab):
        xd = inf
        if aux_tab[n] != inf:
            return aux_tab[n]
        for x in range(tab[0], len(tab)):
            if n - tab[x] >= 0:
                xd = min(xd, reku(tab, n-tab[x], aux_tab)+1)
        aux_tab[n] = xd
        return aux_tab[n]

    n = len(tab)
    aux_tab = [inf]*(k+1)
    for x in range(n):
        aux_tab[tab[x]] = 1
    aux_tab[0] = 0
    reku(tab, k, aux_tab)
    return aux_tab


tab = [1, 2, 5]
k = 97
print(top_down_coin_change_problem(tab, k))
print(bottom_up_coin_change_problem(tab, k))

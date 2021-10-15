# [ENG] Thank to dynamic programming we can find longest increasing subsequence (LIS) of given sequence. So let's
# declare a function: f(i) - LIS which consists of elements only from tab[0] to tab[i].
# Basic case: f(0) = 1, one-piece sequence is a trivial increasing sequence
# Recursion: f(i) = max(f(k))+1, where "k" is a certain index located before index "i", so already computed value f(k)
# informs us about LIS from tab[0] to tab[k]
# Solution: f(n-1) - last element of our auxiliary array
# Note that LIS doesn't have to be unique. A sequence can have several longest increasing subsequences.
# [Pl] Dzięki programowaniu dynamicznemu jesteśmy w stanie znaleźć najdłuższy rosnący podciąg (z ang. LIS) podanego
# ciągu. Funkcja, zależność rekurencyjna oraz sposób odczytywania rozwiązania są podane powyżej w języku angielskim.
# Warto tutaj zauważyć, iż LIS nie musi być jedyny. Pewien ciąg może zawierać kilka lub nawet więcej najdłuższych
# rosnących podciągów.

def lis(tab):
    n = len(tab)
    aux_tab = [1]*n
    parent = [-1]*n
    for x in range(1, n):
        ctr1, ctr2 = 0, -1
        for y in range(x):
            if tab[y] < tab[x]:
                if aux_tab[y] > ctr1:
                    ctr1 = aux_tab[y]
                    ctr2 = y
        aux_tab[x] = ctr1 + 1
        parent[x] = ctr2

    ctr, ctr1 = 0, 0
    for x in range(n):
        if aux_tab[x] > ctr:
            ctr = aux_tab[x]
            ctr1 = x
    return print_solution(parent, ctr1)


def print_solution(parent, x):
    solution = [tab[x]]
    while parent[x] != -1:
        solution.append(tab[parent[x]])
        x = parent[x]
    return solution[::-1]


tab = [100, 40, 2, 5, 7, 2, 4, 9, 3, 17, 3, 1]
print(lis(tab))

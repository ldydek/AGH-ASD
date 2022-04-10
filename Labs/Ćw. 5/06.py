# f(i) - minimalna ilość monet potrzebnych do wydania kwoty "i" złotych
# f(i) = min(f(i-A[k]), gdzie A to tablica nominałów
# Warunki brzegowe: f(A[k]) = 1, 0 <= k <= len(A)-1
# Złożoność obliczeniowa: O(nT)
# Złożoność pamięciowa: O(T)

def ex06(A, T):
    n = len(A)
    aux_tab = [10**10] * (T+1)
    for x in range(n):
        if A[x] < T:
            aux_tab[A[x]] = 1
    mini = min(A)
    for x in range(mini+1, T+1):
        if aux_tab[x] == 1:
            continue
        ctr = 10**10
        for y in range(n):
            ctr = min(ctr, aux_tab[x-A[y]])
        aux_tab[x] = ctr + 1
    return aux_tab[T]


A = [1, 5, 8]
print(ex06(A, 15))

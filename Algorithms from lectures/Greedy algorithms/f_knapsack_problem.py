# Ciągły problem plecakowy. Dla każdego płynu definiujemy współczynnik opłacalności jako: P[i]/Q[i] dla każdego i
# należącego od 0 do n-1, gdzie n=len(W)
# Sortujemy płyny malejąco po współczynnikach opłacalności i wlewamy do butelki tyle wartościowych płynów ile się da,
# począwszy oczywiście od tego najbardziej opłacalnego.


def f_knapsack_problem(W, P, max_w):
    n = len(W)
    T = [(0, 0, 0)]*n
    for x in range(n):
        T[x] = P[x]/W[x], W[x], P[x]
    T.sort(reverse=True)
    ctr1, ctr2 = 0, 0
    while max_w > 0:
        if T[ctr1][1] < max_w:
            max_w -= T[ctr1][1]
            ctr2 += T[ctr1][1] * T[ctr1][0]
            ctr1 += 1
            if ctr1 == n:
                return ctr2
        else:
            ctr2 += T[ctr1][0] * max_w
            return ctr2
    return ctr2


W = [10, 40, 20, 30]
P = [10, 40, 20, 30]
print(f_knapsack_problem(W, P, 50))

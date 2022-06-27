# Na samym początku sortuję podane przedziały malejąco po długościach
# f(i) - najliczniejszy podciąg klocków ze zbioru od A[0] do A[i], który spełnia warunki zadania. Innymi słowy to taki
# podciąg, w którym kolejne klocki w całości zawierają się w poprzednich.
# Rekurencja: f(i) = max(f(i-k)) + 1, 1 <= k <= i
# Rozwiązanie: f(n-1), gdzie "n" to ilość wszystkich klocków


def include(x, y):
    return x[0] <= y[0] and y[1] <= x[1]


def ex02(tab):
    n = len(tab)
    aux_tab = [1] * n
    tab.sort(key=lambda tab: tab[1]-tab[0], reverse=True)
    solution = -10**10
    for x in range(1, n):
        ctr = 0
        for y in range(x):
            if include(tab[y], tab[x]):
                ctr = max(ctr, aux_tab[y])
                solution = max(solution, ctr)
        aux_tab[x] = ctr + 1
    return n - solution - 1


tab = [[1, 5], [2, 7], [3, 4], [1, 10], [3, 3]]
print(ex02(tab))

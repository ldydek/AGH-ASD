# f(i, j) - największy zysk, jaki można uzyskać, rozważając przedmioty od W[0] do W[i], nie przekraczając wagi "j"
# f(i, j) = max(f(i-1, j), f(i-1, j-W[i])+P[i])
# Warunki brzegowe:
# - f(i, 0) = 0
# - f(0, j) = P[0], jeśli W[0] >= j oraz 0 wpp.
# Rozwiązanie: f(n-1, max_w) - "n" to ilość przedmiotów a "max_w" to maksymalna waga, którą jesteśmy w stanie osiągnąć
# Aby odtworzyć rozwiązanie, wystarczy poruszać się od prawego dolnego rogu i sprawdzać, czy wartość w tablicy
# dodatkowej komórkę wyżej jest taka sama. Jeśli tak, to znaczy, że bieżący przedmiot nie został wzięty do rozwiązania.
# Jeśli natomiast został on uwzględniony, to przemieszczamy się w tablicy jeden wiersz do góry oraz "k" jednostek
# w lewo, gdzie "k" to waga uwzględnionego przedmiotu. Dany schemat powtarzamy do momentu spotkania 0 w macierzy.


def ex01(W, P, max_w):
    n = len(W)
    aux_tab = [[0 for _ in range(max_w+1)] for _ in range(n)]
    for x in range(W[0], max_w+1):
        aux_tab[0][x] = P[0]
    for x in range(1, n):
        for y in range(1, max_w+1):
            aux_tab[x][y] = aux_tab[x-1][y]
            if y >= W[x]:
                if aux_tab[x-1][y-W[x]]+P[x] > aux_tab[x][y]:
                    aux_tab[x][y] = aux_tab[x-1][y-W[x]]+P[x]
    return print_solution(aux_tab, n-1, max_w, W)


def print_solution(aux_tab, x, y, W):
    solution = []
    while aux_tab[x][y] != 0:
        if aux_tab[x][y] == aux_tab[x-1][y]:
            x = x - 1
            continue
        solution.append(W[x])
        x, y = x-1, y-W[x]
    return solution[::-1]


W = [10, 3, 5, 8, 3, 7]
P = [12, 4, 50, 70, 2, 10]
print(ex01(W, P, 24))

# f(i) - ilość sposobów pocięcia słowa od t[0] do t[i] tak, aby podział spełniał warunki zadania (w każdym kawałku
# znajdowała się dokładnie jedna samogłoska). Złożoność obliczeniowa: O(n^2), ponieważ przeszukiwanie tablicy letters
# zajmuje czas stały.

def cutting(s):
    n = len(s)
    aux_tab = [0]*(n+1)
    letters = ["a", "ą", "e", "ę", "i", "o", "u", "y"]
    k = 0
    for x in range(1, n+1):
        if s[x-1] in letters:
            aux_tab[x] = 1
            k = x
            break
    for y in range(k, n+1):
        aux_tab[y] = 1
    aux_tab[0] = 1

    for x in range(2, n+1):
        ctr = 0
        suma = 0
        if s[x-1] in letters:
            ctr += 1
        for y in range(x-1, -1, -1):
            if ctr == 1:
                suma += aux_tab[y]
            if s[y-1] in letters:
                ctr += 1
            if ctr > 1:
                break
        aux_tab[x] = suma
    return aux_tab[len(s)]


s = "aaaaa"
print(cutting(s))

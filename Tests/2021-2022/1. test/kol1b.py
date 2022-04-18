# Na samym początku sortuję litery w każdym słowie z tablicy leksykograficznie. Następnie tworzę "n+1" kubełków.
# Do i-tego kubełka wrzucam wszystkie napisy o długości "i". W każdym kubełku elementy sortuję algorytmem sortowania
# pozycyjnego. Potem sprawdzam w każdym kubełku ile takich samych napisów  znajduje się obok siebie, inkrementując
# licznik (jeśli elementy są sobie równe pierwotnie musiały być anagramami). Na sam koniec biorę maksimum ze wszystkich
# wyników w kubełkach.
# Złożoność czasowa: O(n)
# Złożoność pamięciowa: O(n)
from kol1btesty import runtests


def change(A, aux_tab):
    for x in range(len(aux_tab)):
        aux_tab[x] = 0
    for x in range(len(A)):
        aux_tab[ord(A[x])-97] += 1
    new_string = []
    for x in range(len(aux_tab)):
        k = aux_tab[x]
        while k:
            new_string.append(chr(x+97))
            k -= 1
    new_string = ''.join(new_string)
    return new_string


def count_sort(strings, B, C, index):
    for x in range(len(B)):
        B[x] = 0
    for x in range(len(strings)):
        if len(strings[x]) <= index:
            B[0] += 1
        else:
            B[ord(strings[x][index])-96] += 1
    for x in range(1, len(B)):
        B[x] += B[x-1]
    for x in range(len(strings)-1, -1, -1):
        if len(strings[x]) <= index:
            C[B[0]-1] = strings[x]
            B[0] -= 1
        else:
            C[B[ord(strings[x][index])-96]-1] = strings[x]
            B[ord(strings[x][index]) - 96] -= 1
    for x in range(len(strings)):
        strings[x] = C[x]


def string_sort(strings, B, C):
    max_length = len(strings[0])
    for x in range(max_length, -1, -1):
        count_sort(strings, B, C, x)
    return strings


def count_numbers(tab):
    ctr, sol = 0, 0
    for x in range(1, len(tab)):
        if tab[x-1] == tab[x]:
            ctr += 1
            sol = max(sol, ctr)
        else:
            ctr = 0
    return sol


def count_signes(tab):
    ctr = 0
    for x in range(len(tab)):
        ctr += len(tab[x])
    return ctr


def f(T):
    n = len(T)
    aux_tab = [0] * 27
    B = [0] * 27
    C = [0] * n
    for x in range(len(T)):
        T[x] = change(T[x], aux_tab)
    ctr = count_signes(T)
    buckets = [[] for _ in range(ctr + 1)]
    for x in range(len(T)):
        buckets[len(T[x])].append(T[x])
    for x in range(len(buckets)):
        if len(buckets[x]) > 0:
            string_sort(buckets[x], B, C)
    solution = 0
    for x in range(len(buckets)):
        solution = max(solution, count_numbers(buckets[x]))
    return solution + 1


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(f, all_tests=True)

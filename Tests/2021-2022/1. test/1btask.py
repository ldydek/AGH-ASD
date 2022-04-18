# Firstly, I sort letters in each word alphabetically, for instance "wilk" will be "iklw". Later, I create "n+1" 
# buckets. To "i-th" bucket I put all strings of the length "i". In each bucket I sort elements using radix sort. Later,
# I check how many the same strings is next to each other (if strings are the same they had to be anagrams previously).
# At the end, I count maximum value from all buckets.
# Time complexity: O(n)
# Space complexity: O(n)
# Passed all tests
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
        B[ord(strings[x][index])-97] += 1
    for x in range(1, len(B)):
        B[x] += B[x-1]
    for x in range(len(strings)-1, -1, -1):
        C[B[ord(strings[x][index])-97]-1] = strings[x]
        B[ord(strings[x][index]) - 97] -= 1
    for x in range(len(strings)):
        strings[x] = C[x]


def string_sort(strings, B, C):
    max_length = len(strings[0]) - 1
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


# Change all_tests=False to all_tests=True if you want to run all tests.
runtests(f, all_tests=True)

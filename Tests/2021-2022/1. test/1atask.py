# Firstly, we determine which word is lexicographically smaller - previous list element or its reverse. Let's choose
# this one which is smaller and omit the second one. Now after that all words that are equivalent are simply identical.
# Later we put each word to an appropriate bucket which corresponds to its length. In each bucket we sort all words and
# now these ones which are identical are located next to each other. At the, end we have to simply find a place with
# the most identical words located next to each other and return their quantity.
# Time complexity: O(N), where "N" is the length of all words
# Space complexity: O(N)
# Passed all tests
# Time for all tests: ~ 3.10 s

from kol1atesty import runtests


# O(n) - changing certain list elements to their reverses
def change(T):
    n = len(T)
    for x in range(n):
        string = T[x][::-1]
        if string < T[x]:
            T[x] = string


# O(n) - determining length of the longest word and by the way number of all buckets
def get_max_length(T):
    length = 0
    for x in range(len(T)):
        length = max(length, len(T[x]))
    return length


# O(N)
def g(T):
    n = len(T)
    change(T)
    length = get_max_length(T)
    buckets = [[] for _ in range(length)]
    for x in range(n):
        buckets[len(T[x])-1].append(T[x])
    for x in range(len(buckets)):
        if len(buckets[x]) > 0:
            string_sort(buckets[x])
    return get_solution(buckets)


# O(N) - finding the strongest word
def get_solution(buckets):
    solution = 1
    for x in range(len(buckets)):
        value = 1
        for y in range(1, len(buckets[x])):
            if buckets[x][y-1] == buckets[x][y]:
                value += 1
                solution = max(solution, value)
            else:
                value = 1
    return solution


def count_sort(strings, B, C, index):
    for x in range(len(B)):
        B[x] = 0
    for x in range(len(strings)):
        B[ord(strings[x][index])-96] += 1
    for x in range(1, len(B)):
        B[x] += B[x-1]
    for x in range(len(strings)-1, -1, -1):
        C[B[ord(strings[x][index])-96]-1] = strings[x]
        B[ord(strings[x][index]) - 96] -= 1
    for x in range(len(strings)):
        strings[x] = C[x]


# in each bucket we sort strings using radix sort
def string_sort(strings):
    n = len(strings)
    B = [0] * 27
    C = [0] * n
    for x in range(len(strings[0])-1, -1, -1):
        count_sort(strings, B, C, x)
    return strings


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(g, all_tests=True)

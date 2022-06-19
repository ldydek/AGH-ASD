# Idea is similar to the previous version of this tasks, but this time we use radix sort for sorting strings. Before
# it we are forced to put strings of the same length to one bucket. Later, we sort it from the last letter to the first
# one. Rest of the task is the same.
# Time complexity: O(D) - during sorting we consider each letter from each word only once and during determining nice
# strings and very nice we consider twice so it's still O(D)
# Space complexity: O(D)
# Passed all test

# O(n) - function that determines length of the longest string
def get_length(s):
    length = 0
    for x in range(len(s)):
        length = max(length, len(s[x]))
    return length


# O(n) - in that function we consider one letter from at most "n" strings
def count_sort(A, n, index, end):
    C = [0] * 2
    B = [0] * n
    start = index
    while start <= end:
        for x in range(len(A[start])):
            C[int(A[start][x][index-1])] += 1
        start += 1
    for x in range(1, 2):
        C[x] += C[x-1]
    start = index
    aux_end = end
    while start <= aux_end:
        for x in range(len(A[aux_end])-1, -1, -1):
            B[C[int(A[aux_end][x][index-1])]-1] = A[aux_end][x]
            C[int(A[aux_end][x][index-1])] -= 1
        aux_end -= 1
    start = index
    ctr = -1
    while start <= end:
        for x in range(len(A[start])):
            ctr += 1
            A[start][x] = B[ctr]
        start += 1


# O(1) - reading quantity of string from A[start] to A[end] (including both)
def read_array_length(tab, start, end):
    if start == 0:
        return tab[end]
    return tab[end] - tab[start-1]


# O(D) - sorting strings using radix sort
# (during sorting each letter from each string we consider only once so it's O(D))
# D - sum of all letters from all strings
def string_sort(s):
    length = get_length(s)
    buckets = [[] for _ in range(length+1)]
    for x in range(len(s)):
        buckets[len(s[x])].append(s[x])
    array_lengths = [0] * (length + 1)
    array_lengths[0] = len(buckets[0])
    for x in range(1, length+1):
        array_lengths[x] = array_lengths[x-1] + len(buckets[x])
    k = length
    while k:
        n = read_array_length(array_lengths, k, length)
        count_sort(buckets, n, k, length)
        k -= 1
    ctr = -1
    for x in range(len(buckets)):
        for y in range(len(buckets[x])):
            ctr += 1
            s[ctr] = buckets[x][y]
    return s


# O(d) - where "d" is the average length of one string
def prefix(a, b):
    for x in range(len(a)):
        if a[x] != b[x]:
            return False
    return True


# O(D) because of string sorting
def removing_prefixes(tab):
    n = len(tab)
    string_sort(tab)
    taken = [0] * n
    for x in range(1, n):
        if prefix(tab[x-1], tab[x]) is False:
            taken[x-1] = 1
    taken[n-1] = 1
    solution = []
    for x in range(n):
        if taken[x] == 1:
            solution.append(tab[x])
    return solution


# O(D) because of string sorting
def double_prefix(L):
    n, ctr = len(L), 0
    string_sort(L)
    tab = [[]]
    for x in range(1, n):
        for y in range(len(L[x-1])):
            if L[x-1][y] != L[x][y]:
                break
            tab[ctr].append(L[x-1][y])
        if len(tab[ctr]) > 0:
            tab[ctr] = ''.join(tab[ctr])
            ctr += 1
            tab.append([])
    tab.pop()
    return removing_prefixes(tab)


L = ['00001', '00111', '001011', '0001000', '0010001', '0010010', '0100010', '0101111']
print(double_prefix(L))

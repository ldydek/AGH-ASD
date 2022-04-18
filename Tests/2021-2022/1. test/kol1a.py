def change(string):
    new_string = ""
    for x in range(len(string)-1, -1, -1):
        new_string += string[x]
    return new_string


def count_signs(T):
    ctr = 0
    for x in range(len(T)):
        ctr += len(T[x])
    return ctr


def count_sort(tab, B, C, index):
    for x in range(len(B)):
        B[x] = 0
    for x in range(len(tab)):
        B[ord(tab[x][index])-97] += 1
    for x in range(1, len(B)):
        B[x] += B[x-1]
    for x in range(len(tab)-1, -1, -1):
        C[B[ord(tab[x][index])-97] - 1] = tab[x]
        B[ord(tab[x][index]) - 97] -= 1
    for x in range(len(C)):
        tab[x] = C[x]
    return tab


def radix_sort(tab, B, C):
    length = len(tab[0]) - 1
    for x in range(length, -1, -1):
        count_sort(tab, B, C, x)
    return tab


def count_strings(tab):
    ctr, sol = 0, 0
    for x in range(1, len(tab)):
        if tab[x-1] == tab[x]:
            ctr += 1
            sol = max(sol, ctr)
    return sol


def g(T):
    B = [0] * 27
    C = [0] * 3
    ctr = count_signs(T)
    for x in range(len(T)):
        T[x] = T[x], change(T[x])
        if ord(T[x][0][0]) > ord(T[x][1][0]):
            T[x] = T[x][1], T[x][0]
    for x in range(len(T)):
        T[x] = T[x][0]
    buckets = [[] for _ in range(ctr+1)]
    for x in range(len(T)):
        buckets[len(T[x])].append(T[x])
    radix_sort(buckets[4], B, C)
    solution = 0
    for x in range(len(buckets)):
        if len(buckets[x]) > 0:
            solution = max(solution, count_strings(buckets[x]))
    return solution + 1


T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
print(g(T))



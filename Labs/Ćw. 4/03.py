def ex03_a(word1, word2, k):
    n = len(word1)
    if n != len(word2):
        return False
    aux_tab = [0] * k
    for x in range(n):
        aux_tab[ord(word1[x]) - 97] += 1
        aux_tab[ord(word2[x]) - 97] -= 1
    for x in range(k):
        if aux_tab[x]:
            return False
    return True


def ex03_b(word1, word2, k):
    n = len(word1)
    if n != len(word2):
        return False
    aux_tab = [0] * k
    for x in range(n):
        aux_tab[ord(word1[x])-97] += 1
        aux_tab[ord(word2[x])-97] -= 1
    for x in range(n):
        if aux_tab[ord(word1[x])-97]:
            return False
    return True


print(ex03_a("zak", "kza", 26))
print(ex03_b("zat", "zta", 26))

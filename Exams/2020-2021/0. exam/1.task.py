from queue import deque


def tanagram(x, y, t):
    if len(x) != len(y):
        return False
    aux_tab = [deque() for _ in range(26)]
    for i in range(len(x)):
        aux_tab[ord(x[i])-97].append(i)
    for i in range(len(y)):
        if len(aux_tab[ord(y[i])-97]) == 0:
            return False
        if abs(aux_tab[ord(y[i])-97].popleft() - i) > t:
            return False
    return True


x = "egzamin"
y = "gezmina"
t = 4
print(tanagram(x, y, t))



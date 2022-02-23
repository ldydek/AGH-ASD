class Node:
    def __init__(self):
        self.value = 0
        self.next = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


def ex022_1(A, k):
    ctr = 0
    second, first = A, A
    while ctr != k:
        ctr += 1
        second = second.next
    while second:
        second = second.next
        first = first.next
    return first.value


def ex022_2(A, k):
    ctr = 0
    first = A
    while first:
        ctr += 1
        first = first.next
    first = A
    n = ctr
    ctr = 0
    while ctr != n-k:
        ctr += 1
        first = first.next
    return first.value


tab = [1, 10, 2, 6, 24, 3, 15]
A = tab2list(tab)
print_list(A)
print(ex022_1(A, 3))
print(ex022_2(A, 3))

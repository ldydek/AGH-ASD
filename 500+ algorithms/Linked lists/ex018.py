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


def ex018(A, B):
    G = Node()
    start = G
    while A and B:
        if A.value == B.value:
            start.next = A
            start = A
            A = A.next
            B = B.next
        elif A.value > B.value:
            B = B.next
        else:
            A = A.next
    start.next = None
    return G.next


tab1 = [1, 4, 7, 10, 11]
tab2 = [2, 4, 6, 8, 10]
A = tab2list(tab1)
B = tab2list(tab2)
print_list(A)
print_list(B)
print_list(ex018(A, B))

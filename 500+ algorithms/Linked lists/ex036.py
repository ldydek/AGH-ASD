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


def ex036(A):
    odd = Node()
    even = Node()
    odd1 = odd
    even1 = even
    while A:
        if A.value % 2:
            odd1.next = A
            odd1 = A
        else:
            even1.next = A
            even1 = A
        A = A.next
    odd1.next = None
    even1.next = odd.next
    return even.next


tab = [1, 2, 3, 4, 5, 6, 7, 8]
A = tab2list(tab)
print_list(ex036(A))

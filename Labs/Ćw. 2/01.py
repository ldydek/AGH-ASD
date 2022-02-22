# [ENG] 1.1 Merging two linked lists.
# [PL] 1.1 Scalanie dwóch list jednokierunkowych.

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


# [ENG] With guardian
# [PL] Z wartownikiem
def ex01_1_1(A, B):
    start = Node()
    jump = start
    while A and B:
        if A.value < B.value:
            jump.next = A
            A = A.next
            jump = jump.next
        else:
            jump.next = B
            B = B.next
            jump = jump.next
    if not A:
        jump.next = B
    elif not B:
        jump.next = A
    return start.next


# [ENG] Without guardian
# [PL] Bez wartownika
def ex01_1_2(A, B):
    if A.value < B.value:
        start = A
        A = A.next
    else:
        start = B
        B = B.next
    jump = start
    while A and B:
        if A.value < B.value:
            jump.next = A
            A = A.next
            jump = jump.next
        else:
            jump.next = B
            B = B.next
            jump = jump.next
    if not A:
        jump.next = B
    elif not B:
        jump.next = A
    return start


tab1 = [1, 4, 5, 10, 14, 15, 16]
tab2 = [2, 2, 4, 7, 11]
A = tab2list(tab1)
B = tab2list(tab2)
print_list(A)
print_list(B)
print_list(ex01_1_1(A, B))
print_list(ex01_1_2(A, B))
# [ENG] Note that I can't execute both functions, but only one of them.
# [PL] Warto zauważyć, że nie mogę wykonać tych dwóch funkcji a jedynie jedną z nich.

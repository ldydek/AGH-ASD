# [ENG] Reversing a linked list recursively.
# [PL] Rekurencyjne odwracanie listy jednokierunkowej.

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


def ex020(A):
    back, middle, front = None, A, A.next
    solution = ex020_recur(back, middle, front)
    return solution


def ex020_recur(back, middle, front):
    if front:
        middle.next = back
        back = middle
        middle = front
        front = front.next
        return ex020_recur(back, middle, front)
    middle.next = back
    return middle


tab = [1, 10, 2, 3, 4, 2]
A = tab2list(tab)
print_list(A)
print_list(ex020(A))

# [ENG] Detecting cycle in a linked list.
# [PL] Wykrywanie cyklu w liście jednokierunkowej.

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
    C.next = H.next
    return H.next


def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


def ex030(A):
    back, front = A, A
    while front and front.next:
        back = back.next
        front = front.next.next
        if front == back:
            return True
    return False


tab = [1, 2, 3, 4, 5, 6, 7, 8]
A = tab2list(tab)
print(ex030(A))

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


def ex022(A):
    zero1 = Node()
    first = Node()
    second = Node()

    zero = zero1
    one = first
    two = second

    back = A
    front = A.next
    while back:
        if back.value == 0:
            zero.next = back
            zero = zero.next
            zero.next = None
        elif back.value == 1:
            one.next = back
            one = one.next
            one.next = None
        else:
            two.next = back
            two = two.next
            two.next = None
        back = front
        if front:
            front = front.next
    zero.next = first.next if first.next else second.next
    one.next = second.next
    return zero1.next


tab = [1, 1, 0, 0, 2, 1, 2, 0, 1, 0, 2, 1]
A = tab2list(tab)
print_list(A)
print_list(ex022(A))

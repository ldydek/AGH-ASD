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


def ex026(A):
    slow, fast = A, A.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    stay = slow
    slow = slow.next
    stay.next = None
    slow, fast = reverse(slow), A
    add1, add2 = fast.next, slow.next
    while add2:
        fast.next = slow
        slow.next = add1
        fast = add1
        slow = add2
        add1 = add1.next
        add2 = add2.next
    fast.next = slow
    slow.next = add1
    return A


def reverse(A):
    if not A:
        return None
    elif not A.next:
        return A
    back = None
    middle = A
    front = A.next
    while front:
        middle.next = back
        back = middle
        middle = front
        front = front.next
    middle.next = back
    return middle


tab = [1, 2, 3, 4, 5, 6, 7, 8]
A = tab2list(tab)
print_list(A)
print_list(ex026(A))

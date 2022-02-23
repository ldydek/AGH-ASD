# [ENG] Removing duplicates.
# [PL] Usuwanie duplikatów.

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


def partition(A, end):
    if A is None or end is None:
        return
    start = A
    edge = start
    prev = edge
    while A != end:
        A = A.next
    pivot = A
    A = start
    while A != end:
        if A.value <= pivot.value:
            prev = edge
            curr = A.value
            A.value = edge.value
            edge.value = curr
            edge = edge.next
        A = A.next
    curr = edge.value
    edge.value = pivot.value
    A.value = curr
    return prev


def quick_sort(A, end):
    start = A
    A = start
    if A != end:
        q = partition(A, end)
        quick_sort(A, q)
        if q.next != end:
            q_next = q.next.next
            quick_sort(q_next, end)
    return A


def quicksort(A):
    start = A
    while A.next:
        A = A.next
    end = A
    A = quick_sort(start, end)
    return A


# O(n lg n)
def ex034(A):
    quicksort(A)
    back = None
    front = A
    while front:
        while back and front and back.value == front.value:
            back.next = front.next
            front = front.next
        if front:
            back = front
            front = front.next
    return print_list(A)


tab = [5, 3, 4, 2, 5, 4, 1, 3]
A = tab2list(tab)
print_list(A)
ex034(A)

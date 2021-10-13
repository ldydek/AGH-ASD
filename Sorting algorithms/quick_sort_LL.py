# Quick Sort na listach jednokierunkowych.


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


tab = [1, 4, 7, 7, 1, 1, 2, 10, 13, 3, 6, 9]
A = tab2list(tab)
print_list(A)
start = A
while A.next:
    A = A.next
end = A
A = start
# print(quick_sort(A, end))
(quick_sort(A, end))
print_list(A)

# [ENG] Quick sort algorithm on linked lists. Firstly, we change Python list to linked list and then sort it.
# Time complexity: O(n lg n)
# [PL] Sortowanie szybkie wykonane na listach jednokierunkowych. Na początku zmieniamy listę w Pythonie na
# listę jednokierunkową a następnie wykonujemy samo sortowanie.
# Złożoność czasowa: O(n lg n)

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
    quick_sort(start, end)


tab = [10, 2, 5, 5, 10, 1, 1, 3, 3, 2, 7]
A = tab2list(tab)
print_list(A)
quicksort(A)
print_list(A)

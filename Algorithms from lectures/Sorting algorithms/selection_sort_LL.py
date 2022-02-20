# [ENG] Selection sort algorithm on linked lists. Firstly, we change Python list to linked list and then sort it.
# Whilst algorithm is running, additionally I use functions for deleting maximum element and inserting it in an
# appropriate place.
# Time complexity: O(n^2)
# [PL] Sortowanie przez wybieranie wykonane na listach jednokierunkowych. Na początku zmieniamy listę w Pythonie na
# listę jednokierunkową a następnie wykonujemy samo sortowanie. Podczas działania algorytmu korzystam w pomocniczych
# funkcji, które usuwają maksimum z jednej listy i dodają do drugiej w odpowiednie miejsce.
# Złożoność czasowa: O(n^2)

from math import inf


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


def insertion_to_sorted_list(A, x):
    if not A:
        A = x
        return A
    x.next = A
    return x


def deleting_max_from_list(A):
    if not A:
        return None
    start = A
    x = -inf
    while start:
        x = max(x, start.value)
        start = start.next
    start, back = A, A
    while start.value != x:
        back = start
        start = start.next
    if start == A:
        back = start.next
        start.next = None
        return x, back
    back.next = start.next
    return x, A


def selection_sort(A):
    ctr, start = 0, A
    B = None
    while start:
        start = start.next
        ctr += 1
    for x in range(0, ctr):
        X = Node()
        X.value, A = deleting_max_from_list(A)
        B = insertion_to_sorted_list(B, X)
    return B


tab = [2, 7, 1, 3, 20, 4, 30, 1, 1]
A = tab2list(tab)
print_list(A)
print_list(selection_sort(A))

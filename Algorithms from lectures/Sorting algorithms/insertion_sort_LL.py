# [ENG] Insertion sort algorithm on linked lists. Firstly, we change Python list to linked list and then sort it.
# Whilst algorithm is running, additionally I use functions for deleting certain element and inserting it in an
# appropriate place.
# Time complexity: O(n^2)
# [PL] Sortowanie przez wstawianie wykonane na listach jednokierunkowych. Na początku zmieniamy listę w Pythonie na
# listę jednokierunkową a następnie wykonujemy samo sortowanie. Podczas działania algorytmu korzystam w pomocniczych
# funkcji, które usuwają pewien element z jednej listy i dodają do drugiej w odpowiednie miejsce.
# Złożoność czasowa: O(n^2)


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


def deleting_element(A, x):
    ctr = 0
    back, front = None, A
    while ctr != x:
        back = front
        front = front.next
        ctr += 1
    back.next = front.next
    return front


def inserting_element(A, X, x):
    back, front = None, A
    y = 0
    while y < x and front.value < X.value:
        back = front
        front = front.next
        y += 1
    if back:
        back.next = X
        X.next = front
        return A
    X.next = front
    return X


def insertion_sort(A):
    n = 0
    front = A
    while front:
        n += 1
        front = front.next
    for x in range(1, n):
        X = deleting_element(A, x)
        A = inserting_element(A, X, x)
    return A


tab = [2, 7, 1, 3, 20, 4, 30, 1, 1]
A = tab2list(tab)
print_list(A)
print_list(insertion_sort(A))

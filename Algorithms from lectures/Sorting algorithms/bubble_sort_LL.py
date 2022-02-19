# [ENG] Bubble sort algorithm on linked lists. Firstly, we change Python list to linked list and then sort it.
# Time complexity: O(n^2)
#
# [PL] Algorytm sortowania bąbelkowego wykonany na listach jednokierunkowych. Na początku zamieniamy listę Pythonową
# na listę jednokierunkową, a następnie ją sortujemy.
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


def bubble_sort(T):
    if T.next is None:
        return T
    ctr = T
    while ctr:
        back = T
        middle = T.next
        front = T.next.next
        if back.value > middle.value:
            middle.next = back
            back.next = front
            curr = middle
            middle = back
            back = curr
            T = back
        while front:
            if middle.value > front.value:
                middle.next = front.next
                back.next = front
                front.next = middle
                curr = middle
                middle = front
                front = curr
            back = back.next
            middle = middle.next
            front = front.next
        ctr = ctr.next
    return T


tab = [2, 2, 2, 1, 5, 10, 50, 3, 34]
T = tab2list(tab)
print_list(T)
T = bubble_sort(T)
print_list(T)

# [ENG] Merge sort algorithm on linked lists. Firstly, we change Python list to linked list and then sort it.
# Time complexity: O(n lg n)
# [PL] Sortowanie przez scalanie wykonane na listach jednokierunkowych. Na początku zmieniamy listę w Pythonie na
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


def get_middle(A):
    if A is None:
        return A
    slow = A
    fast = A
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sort(A):
    if A.next is None:
        return A
    middle = get_middle(A)
    middle_next = middle.next
    middle.next = None
    left = merge_sort(A)
    right = merge_sort(middle_next)
    C1 = merge(left, right)
    return C1


def merge(A, B):
    if A.value < B.value:
        result = A
        A = A.next
    else:
        result = B
        B = B.next
    start = result
    while A and B:
        if A.value < B.value:
            result.next = A
            A = A.next
            result = result.next
        else:
            result.next = B
            B = B.next
            result = result.next
    while A:
        result.next = A
        A = A.next
        result = result.next
    while B:
        result.next = B
        B = B.next
        result = result.next
    return start


tab = [1, 2, 7, 3, 10, 3, 2, 18, 3, 7]
A = tab2list(tab)
print_list(A)
merge_sort(A)
print_list(A)

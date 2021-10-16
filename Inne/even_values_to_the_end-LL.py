# Program przekształcający listę jednokierunkową w takim sposób, aby wszystkie liczby nieparzyste występowały przed
# parzystymi. Bardzo podobny pomysł do sortowania przez scalanie tylko podczas scalania nie interesuje nas relacja
# większości a relacja parzystości. O(n log n)

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
    # print_list(A)
    # print_list(middle_next)
    left = merge_sort(A)
    right = merge_sort(middle_next)
    C1 = merge(left, right)
    # print_list(C1)
    return C1


def merge(A, B):
    if A.value % 2 == 1 and B.value % 2 == 0:
        result = A
        A = A.next
    else:
        result = B
        B = B.next
    start = result
    while A and B:
        if A.value % 2 == 1 and B.value % 2 == 0:
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


tab = [2, 3, 5, 7, 13, 4, 10, 11, 17]
T = tab2list(tab)
print_list(T)
C = merge_sort(T)
print_list(C)

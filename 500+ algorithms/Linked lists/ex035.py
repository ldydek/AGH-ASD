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


# O(n lg n)
def ex035_b(A):
    quicksort(A)
    n, start = 0, A
    while start:
        start = start.next
        n += 1
    n = (n+1)/2
    ctr, start = 1, A
    while ctr < n:
        ctr += 1
        start = start.next
    front, front1 = start.next, start.next.next
    start.next = None
    start, start1 = A, A.next
    while front1:
        start.next = front
        front.next = start1
        start = start1
        start1 = start1.next
        front = front1
        front1 = front1.next
    start.next = front
    front.next = start1
    return A


# O(n)
def ex035_g(A):
    back, front = A, A.next
    while front and front.next:
        for x in range(2):
            if back.value > front.value:
                val = back.value
                back.value = front.value
                front.value = val
            back = front.next
        front = front.next.next
    if back.value > front.value:
        val = back.value
        back.value = front.value
        front.value = val
    return A


tab = [9, 6, 8, 3, 7, 1]
A = tab2list(tab)
print_list(A)
# print_list(ex035_b(A))
print_list(ex035_g(A))

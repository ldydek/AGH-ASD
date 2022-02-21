# [ENG] Bucket sort algorithm on linked lists. Firstly, we change Python list to linked list and then sort it.
# Time complexity: O(n)
# [PL] Sortowanie kubełkowe wykonane na listach jednokierunkowych. Na początku zmieniamy listę w Pythonie na
# listę jednokierunkową a następnie wykonujemy samo sortowanie.
# Złożoność czasowa: O(n)

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


def inserting_element(A, X):
    if not A:
        A = X
        X.next = None
        return A
    back, front = None, A
    while front and front.value < X.value:
        back = front
        front = front.next
    if back:
        back.next = X
        X.next = front
        return A
    X.next = front
    return X


def bucket_sort(A):
    buckets = [None] * 10
    back, front = A, A.next
    while front:
        buckets[back.value//10] = inserting_element(buckets[back.value//10], back)
        back = front
        front = front.next
    buckets[back.value//10] = inserting_element(buckets[back.value//10], back)
    start = None
    for x in range(10):
        if buckets[x]:
            start = buckets[x]
            break
    jump, k = None, False
    for x in range(10):
        if buckets[x] and k:
            jump.next = buckets[x]
        while buckets[x]:
            jump = buckets[x]
            buckets[x] = buckets[x].next
            k = True
    return start


tab = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68, 7, 99, 95, 97, 99, 7]
A = tab2list(tab)
print_list(A)
print_list(bucket_sort(A))


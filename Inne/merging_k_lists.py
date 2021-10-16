class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def show(first):
    if first == None:
        print("pusta")
    else:
        while first:
            print(first, end ='->')
            first = first.next
        print('None')


def merge(a, b):
    start = a
    guard = a
    a = a.next
    b = b.next
    while a.next and b.next:
        if a.value < b.value:
            guard.next = a
            a = a.next
            guard = guard.next
        else:
            guard.next = b
            b = b.next
            guard = guard.next
    while a:
        guard.next = a
        a = a.next
        guard = guard.next
    while b:
        guard.next = b
        b = b.next
        guard = guard.next
    return start


def add_guard(tab):
    for x in range(len(tab)):
        H = Node()
        A = tab2list(tab[x])
        H.next = A
        tab[x] = H


def merging_k_lists(tab):
    k = len(tab)
    add_guard(tab)
    while True:
        ctr = 0
        while ctr <= k//2:
            show(tab[ctr])
            show(tab[ctr+1])
            xd = merge(tab[ctr], tab[ctr+1])
            ctr += 2
            # show(xd)
        k -= ctr//2


A = [[2, 3, 6, 7], [3, 5, 8, 9, 10], [2, 5, 8, 11, 15], [50, 70, 90], [30, 50, 80, 90]]
print(merging_k_lists(A))

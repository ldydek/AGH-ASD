# Firstly, I allocate additional array to store results after inorder traversal of the given BST tree. After this,
# additional array keeps sorted nodes by their values. At the end, I can simply pin a pointers of a considered element
# to its left and right child and also parent computing their indexes in an array just like in a binary heap.
# Time complexity: O(n)
# Space complexity: O(n)
# Passed all tests
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = 0


def inorder_traversal(a, heap):
    if a is None:
        return
    inorder_traversal(a.left, heap)
    heap.append(a)
    inorder_traversal(a.right, heap)


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def parent(i):
    return (i-1)//2


def ConvertTree(a):
    heap = []
    inorder_traversal(a, heap)
    n = len(heap)
    for x in range(len(heap)):
        heap[x].left = None
        heap[x].right = None
        heap[x].parent = None
    for x in range(len(heap)):
        l = left(x)
        r = right(x)
        p = parent(x)
        if l < n:
            heap[x].left = heap[l]
        if r < n:
            heap[x].right = heap[r]
        if x != 0:
            heap[x].parent = heap[p]
    return heap[0]


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.value = 11
B.value = 3
C.value = 13
D.value = 2
E.value = 7
F.value = 5
A.left = B
A.right = C
B.left = D
B.right = E
B.parent = A
C.parent = A
D.parent = A
E.left = F
E.parent = B
F.parent = E
print(ConvertTree(A))

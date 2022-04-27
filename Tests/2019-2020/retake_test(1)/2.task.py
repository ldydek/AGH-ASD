# Idea is to after pinning created node (let's call it "x") at the beginning look at the next node and its first element
# in a "next" list. It holds information to which node we should set a new pointer from "x". Later, we jump to this
# node and again we read information to which node we should set a new pointer, but this time we don't read first
# element of a "next" list but second. Later, we will read third one if necessary in a next node somewhere in a front
# and so on.
# Time complexity: O(log n) - adding one element at the beginning
# Passed all test

class FastListNode:
    def __init__(self, a):
        self.a = a
        self.next = []

    def __str__(self):
        res = 'a:' + str(self.a) + '\t' + 'next keys:'
        res += str([n.a for n in self.next])
        return res


# ctr - which data from "next" list of the given node we should read
def fast_list_prepend(L, a):
    x = FastListNode(a)
    if L is None:
        return x
    x.next.append(L)
    y = x.next[0]
    ctr = 0
    while y.next:
        # if this condition happens it means that adding a new pointer to first node ("x") is not necessary
        if ctr >= len(y.next):
            break
        # creating a pointer
        x.next.append(y.next[ctr])
        # jumping
        y = y.next[ctr]
        ctr += 1
    return x

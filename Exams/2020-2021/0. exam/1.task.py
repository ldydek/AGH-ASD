# At the beginning, I check if given two strings have the same length. Later, I create 26 queues. First one will be
# storing indexes on which there is "a" letter in a first word, second one - "b" letter etc. Now I consider second word
# and if I want pop from empty queue it means that these words are not anagrams at all. Otherwise, they are anagrams.
# I start popping elements from these queues and remember the greatest difference between indexes. If it is smaller or
# equal to "t" it means that these words are t-anagrams. Allocating queues here is a good option, because, for instance,
# if these words have two letters "o" we have to somehow compare smaller indexes with "o" letters between first and 
# second word, second smaller indexes etc. Of course, approach with two arrays can also work.
# Time complexity: O(n)
# Space complexity: O(n)

from queue import deque


def tanagram(x, y, t):
    if len(x) != len(y):
        return False
    aux_tab = [deque() for _ in range(26)]
    for i in range(len(x)):
        aux_tab[ord(x[i])-97].append(i)
    for i in range(len(y)):
        if len(aux_tab[ord(y[i])-97]) == 0:
            return False
        if abs(aux_tab[ord(y[i])-97].popleft() - i) > t:
            return False
    return True


x = "egzamin"
y = "gezmina"
t = 4
print(tanagram(x, y, t))



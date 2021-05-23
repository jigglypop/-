from pprint import pprint
from itertools import permutations

# 1. 순열 itertools
words = ['A', 'B', 'C', 'D', 'E']
comb = list(permutations(words, 2))

# 2. 순열
r = 2
result = []


def perm(k, used, choice):
    if k == r:
        result.append(choice[::])
        return
    for i in range(len(words)):
        if used & (1 << i):
            continue
        choice.append(words[i])
        perm(k+1, used | (1 << i), choice)
        choice.pop()


perm(0, 0, [])
print(result)

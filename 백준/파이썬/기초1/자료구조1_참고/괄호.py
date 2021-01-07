import sys
from pprint import pprint
sys.stdin = open('9012.txt', 'r')


def isPS(PS):
    S = []
    for p in PS:
        if p == '(':
            S.append(p)
        elif p == ')':
            if S:
                S.pop()
            else:
                return 'NO'
    return 'YES' if not S else 'NO'


for _ in range(int(input())):
    PS = list(input())
    print(isPS(PS))

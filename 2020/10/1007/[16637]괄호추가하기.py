import sys
from collections import defaultdict
sys.stdin = open('16637.txt', 'r')


N = int(input())
s = input()
ans = -sys.maxsize
calc = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y}


def perm(i, res):
    global ans
    if i == N:
        ans = max(res, ans)
        return
    perm(i+2, calc[s[i]](res, int(s[i+1])))
    if i == N-2:
        return
    a = int(s[i+1])
    o = s[i+2]
    b = int(s[i+3])
    perm(i+4, calc[s[i]](res, calc[o](a, b)))


perm(1, int(s[0]))
print(ans)

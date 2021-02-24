import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1243.txt', 'r')
N = int(input())
L = int(input())
h = {}
DP = [[[-1] * 2 for _ in range(1501)] for _ in range(31)]
words = set()
for _ in range(N):
    temp = input()
    for i in range(len(temp)):
        words.add(temp[:i])
        words.add(temp[i:])
words = list(words)
for i in range(len(words)):
    h[words[i]] = i


def check(x, y, length):
    for i in range(length):
        if x[i] != y[len(y)-i-1]:
            return False
    return True


def go(length, S, D):
    if DP[length][S][D] != -1:
        return DP[length][S][D]
    if length == 0:
        if check(S, S, len(S)):
            DP[length][S][D] = 1
            return 1
        else:
            DP[length][S][D] = 0
            return 0
    DP[length][S][D] = 0

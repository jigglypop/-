import sys
from pprint import pprint
sys.stdin = open('2922.txt', 'r')

input = sys.stdin.readline

words = input()
DP = [[[[-1]*(2) for i in range(4)]
       for j in range(4)] for k in range(len(words)+1)]


def go(k, i, j, l):
    if k == len(words):
        return l
    if i >= 3 or j >= 3:
        return 0
    if DP[k][i][j][l] != -1:
        return DP[k][i][j][l]
    temp = 0
    if words[k] == '_':
        temp = go(k+1, i+1, 0, l) * 5 + \
            go(k+1, 0, j+1, l) * 20 + go(k+1, 0, j+1, 1)
    elif words[k] in ['A', 'E', 'I', 'O', 'U']:
        temp = go(k+1, i+1, 0, l)
    elif words[k] == 'L':
        temp = go(k+1, 0, j+1, 1)
    else:
        temp = go(k+1, 0, j+1, l)
    DP[k][i][j][l] = temp
    return temp


print(go(0, 0, 0, 0))

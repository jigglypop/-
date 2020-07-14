import sys
from copy import deepcopy
sys.stdin = open("subtree.txt", 'r')


def SUBTREE(S):
    global c
    if sum(tree[S]) == 0:
        return
    for i in range(2):
        if tree[S][i] != 0:
            c += 1
            SUBTREE(tree[S][i])


T = int(input())
for tc in range(1, T+1):
    E, S = map(int, input().split())
    m = list(map(int, input().split()))
    V = max(m)
    M = [[m[i], m[i+1]] for i in range(0, E*2, 2)]
    tree = [[0, 0] for _ in range(V+1)]
    for u, v in M:
        if tree[u][0] == 0:
            tree[u][0] = v
        else:
            tree[u][1] = v
    c = 1
    SUBTREE(S)
    print('#{} {}'.format(tc, c))

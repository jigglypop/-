import sys
from copy import deepcopy
sys.stdin = open("이진탐색.txt", 'r')

# 중위순회

# 함수형


def BINARY_SEARCH():
    R = [0]

    def INORDER_SEARCH(n):
        if n > N:
            return
        INORDER_SEARCH(tree[n][0])
        R.append(n)
        INORDER_SEARCH(tree[n][1])
    INORDER_SEARCH(1)
    return R


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[i*2, i*2+1] for i in range(N+1)]
    R = BINARY_SEARCH()
    print('#{} {} {}'.format(tc, R.index(1), R.index(N//2)))

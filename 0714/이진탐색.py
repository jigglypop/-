import sys
from copy import deepcopy
sys.stdin = open("이진탐색.txt", 'r')

# 중위순회

# 함수형
# def INORDER_SEARCH(n):
#     global R
#     if n > N:
#         return
#     INORDER_SEARCH(tree[n][1])
#     R.append(n)
#     INORDER_SEARCH(tree[n][2])


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [[i//2, i*2, i*2+1, 0] for i in range(N+1)]
#     R = [0]
#     INORDER_SEARCH(1)
#     print('#{} {} {}'.format(tc, R.index(1), R.index(N//2)))

# 클래스형
class Tree:
    def __init__(self, N):
        self.list = [0] * (N+1)
        self.N = N
        self.cnt = 1
        self.numbering(1)

    def numbering(self, num):
        if num <= N:
            self.numbering(num * 2)
            self.list[num] = self.cnt
            self.cnt += 1
            self.numbering(num*2 + 1)

    def result(self):
        return ' '.join(map(str, (self.list[1], self.list[self.N // 2])))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = Tree(N)
    print('#{} {}'.format(tc, tree.result()))

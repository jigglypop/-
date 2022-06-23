import sys
from math import *
sys.stdin = open("./text/5419.txt", "r")
input = sys.stdin.readline

for _ in range(int(input())):
    board = []
    for _ in range(int(input())):
        a, b = map(int, input().strip().split())
        board.append([a, b])
    board.sort(key = lambda x : (-x[1], x[0]))
    # 좌표 압축
    nums = []
    for i in range(len(board)):
        x, y = board[i]
        if len(nums) == 0:
            nums.append([x, 0])
        else:
            if board[i -1][1] == y:
                nums.append([x, nums[-1][1]])
            else:
                nums.append([x, nums[-1][1] + 1])
    Y = nums[-1][1] + 1
    nums.sort(key = lambda x :(x[0], -x[1]))
    tree = [0] * (4 * Y)
    result = 0

    def query(l, r):
        result = 0
        while l <= r:
            if l % 2 == 1:
                result += tree[l]
                l += 1
            if r % 2 == 0:
                result += tree[r]
                r -= 1
            l //= 2
            r //= 2
        return result

    def update(n, diff):
        while n >= 1:
            tree[n] += diff
            n //= 2

    print("---")
    for _, y in nums:
        y += Y - 1
        result += query(Y + 1, y)
        print(query(Y + 1, y))
        print(tree, y, 2 * Y)
        update(y, 1)
    print(result)
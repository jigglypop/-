import sys
sys.stdin = open('./text/3653.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    N, M = Split()
    tree = [0] * (N + M + 1)
    board = [0] * (N + 1)
    l = N + M

    def update(i, x):
        while i <= l:
            tree[i] += x
            i += (i & -i)

    def sum(i):
        result = 0
        while i > 0:
            result += tree[i]
            i -= (i & -i)
        return result

    for i in range(1, N+1):
        update(M + i, 1)
        board[i] = M + i

    nums = List()
    for i in range(len(nums)):
        num = nums[i]
        print(sum(board[num]-1), end=" ")
        update(board[num], -1)
        board[num] = M - i
        update(board[num], 1)
    print()
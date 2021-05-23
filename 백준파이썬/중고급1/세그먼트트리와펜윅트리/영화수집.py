import sys
sys.stdin = open("3653.txt", "r")
input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())
    tree = [0] * (N + M + 1)
    position = [0] * (N+1)
    l = N + M

    def update(i, diff):
        while i <= l:
            tree[i] += diff
            i += (i & -i)

    def sum(i):
        result = 0
        while i > 0:
            result += tree[i]
            i -= (i & -i)
        return result

    for i in range(1, N+1):
        update(M+i, 1)
        position[i] = M + i

    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        num = nums[i]
        print(sum(position[num]-1), end=" ")
        update(position[num], -1)
        position[num] = M - i
        update(position[num], 1)
    print()

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("5676.txt", "r")
input = sys.stdin.readline


def update(i, x):
    while i < len(tree):
        if x > 0:
            tree[i] *= 1
        elif x < 0:
            tree[i] *= -1
        else:
            tree[i] *= 0
        i += (i & -i)


while True:
    start = input()
    if not start:
        break
    N, K = map(int, start.split())
    nums = [0] + list(map(int, input().split()))
    tree = [1] * (N + 1)
    for i in range(1, len(nums)):
        update(i, nums[i])
    # print(tree)
    for _ in range(K):
        q, a, b = map(str, input().split())
        a = int(a)
        b = int(b)
        if q == 'C':
            i = a
            # if b > 0:
            #     nums[i] = 1
            # elif b < 0:
            #     nums[i] = -1
            # else:
            #     nums[i] = 0
            update(i, b)
            print(tree)
            # print('change')
    #     else:
    #         print('plus')
    # print('---')

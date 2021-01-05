import sys
sys.stdin = open('16943.txt', 'r')

A, B = map(int, input().split())
nums = list(map(int, list(str(A))))
nums.sort(reverse=True)
results = []
N = len(nums)
sum_results = []


def perm(k, chosen, used, sums):
    if k == N:
        print(sums)
        exit(0)
    for i in range(N):
        if (1 << i) & used:
            continue
        if len(chosen) == 0 and nums[i] == 0:
            continue
        temp = sums + nums[i] * 10 ** (N-k-1)
        if temp >= B:
            continue
        perm(k+1, chosen+[nums[i]], used | (1 << i),
             temp)


perm(0, [], 0, 0)
print(-1)

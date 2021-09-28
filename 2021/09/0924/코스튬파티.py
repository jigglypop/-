import sys
sys.stdin = open('./text/6159.txt', 'r')
input = sys.stdin.readline
N, S = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()
j = N - 1
count = 0
for i in range(N):
    if nums[i] > S // 2:
        break
    while nums[i] + nums[j] > S:
        j -= 1
    count += j - i
print(count)
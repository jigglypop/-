import sys
sys.stdin = open("1208.txt", "r")
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
m = n//2
n = n-m
first = [0]*(1 << n)
for i in range(1 << n):
    for k in range(n):
        if (i & (1 << k)) > 0:
            first[i] += a[k]
second = [0]*(1 << m)
for i in range(1 << m):
    for k in range(m):
        if (i & (1 << k)) > 0:
            second[i] += a[k+n]
first.sort()
second.sort(reverse=True)
N = (1 << n)
M = (1 << m)
left = 0
right = 0
result = 0
while left < N and right < M:
    if first[left] + second[right] == s:
        left_cnt = 1
        right_cnt = 1
        left += 1
        right += 1
        while left < N and first[left] == first[left-1]:
            left_cnt += 1
            left += 1
        while right < M and second[right] == second[right-1]:
            right_cnt += 1
            right += 1
        result += left_cnt * right_cnt
    elif first[left] + second[right] < s:
        left += 1
    else:
        right += 1
if s == 0:
    result -= 1
print(result)

import sys
from collections import defaultdict
sys.stdin = open("2015.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]
count = defaultdict(int)
count[0] = 1  # s[0] = 0
ans = 0
for i in range(1, n+1):
    print(count)
    ans += count[s[i]-m]
    count[s[i]] += 1
print(ans)

import sys
sys.stdin = open('10986.txt', 'r')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
mods = [1] + [0] * m
count = 0
mod = 0
for num in nums:
    mod = (mod + num) % m
    count += mods[mod]
    mods[mod] += 1
print(count)

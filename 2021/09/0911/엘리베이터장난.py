import sys
sys.stdin = open('14936.txt', 'r')
input = sys.stdin.readline
N, m = map(int, input().split())
alls = 0
even = 0
odd = 0
k = 0

for i in range(1, N + 1):
    alls |= (1 << i)
    if i % 2 == 0:
        even |= (1 << i)
    if i % 2 == 1:
        odd |= (1 << i)
    if (i - 1) % 3 == 0:
        k |= (1 << i)
print(alls)
print(even)
print(odd)
print(k)


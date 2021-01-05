import sys
sys.stdin = open('2531.txt', 'r')
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
succi = [int(input()) for _ in range(N)]
Max = 0
for i in range(N):
    Max = max(Max, len(set(succi[i:i+k] + succi[:max(0, k-N+i)] + [c])))
print(Max)

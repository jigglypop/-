import sys

sys.stdin = open('input.txt', 'r')


def subset(k, n, cnt, cur_sum):
    global ans, N, K
    if cnt > N or cur_sum > K:
        return
    if k == n:
        if cnt == N and cur_sum == K:
            ans += 1
            return
    subset(k+1, n, cnt+1, cur_sum + k)
    subset(k+1, n, cnt, cur_sum)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    bits = [0] * N
    ans = 0
    subset(1, 13, 0, 0)
    print('#{} {}'.format(tc, ans))

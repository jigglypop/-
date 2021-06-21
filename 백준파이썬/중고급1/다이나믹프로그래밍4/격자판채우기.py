import sys
sys.stdin = open('1648.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
DP = [[0] * (1 << M) for num in range(N * M + 1)]
DP[N * M][0] = 1
for num in reversed(range(N * M)):
    for state in range(1 << M):
        # 첫번째 칸 채워짐
        if state & 1:
            DP[num][state] = DP[num + 1][state >> 1]
        # 아닐 경우
        else:
            if num < (N-1) * M:
                # 아래 격자 놓기
                DP[num][state] += DP[num + 1][(1 << (M - 1)) | (state >> 1)]
                # 두 칸 밀 때 채워졌는지
            if num % M != M-1 and not state & 2:
                # 옆 격자 놓기
                DP[num][state] += DP[num + 2][state >> 2]
print(DP[0][0] % 9901)

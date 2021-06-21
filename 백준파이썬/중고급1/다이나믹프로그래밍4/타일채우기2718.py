import sys
sys.stdin = open('2718.txt', 'r')
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    DP = [[0] * (1 << 4) for num in range(N * 4 + 1)]
    DP[N * 4][0] = 1
    for num in reversed(range(N * 4)):
        for state in range(1 << 4):
            if state & 1:
                DP[num][state] = DP[num + 1][state >> 1]
            else:
                if num < (N-1) * 4:
                    DP[num][state] += DP[num +
                                         1][(1 << (4 - 1)) | (state >> 1)]
                if num % 4 != 4-1 and not state & 2:
                    DP[num][state] += DP[num + 2][state >> 2]
    print(DP[0][0])

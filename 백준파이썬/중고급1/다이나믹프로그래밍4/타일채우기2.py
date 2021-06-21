import sys
sys.stdin = open('13976.txt', 'r')
input = sys.stdin.readline
n = int(input())
Tile = [0]*31
Tile[2] = 3  # N이 2인 경우의 수
# DP
for i in range(4, 31, 2):
    Tile[i] = Tile[2] * Tile[i - 2]  # N-2의 경우의 수 x 가로가 2인 타일묶음
    for j in range(4, i, 2):
        Tile[i] += 2 * Tile[i - j]  # 새로운 경우의 수
    Tile[i] += 2  # 가로가 N인 타일묶음 또다른 새로운 경우의 수

print(Tile[n])

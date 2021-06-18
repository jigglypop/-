import sys
from pprint import pprint
sys.stdin = open("1014.txt", "r")
input = sys.stdin.readline
N = 0
M = 0
board = []


def isOn(state, i):
    return state & (1 << i) > 0


def check(row, state):
    for i in range(M-1):
        if isOn(state, i) and isOn(state, i+1):
            return False
    for i in range(M):
        if board[row][i] == 'x' and isOn(state, i):
            return False
    return True


for _ in range(int(input())):
    N, M = map(int, input().split())
    board = [list(input().replace("\n", "")) for _ in range(N)]
    DP = [[0] * (1 << 10) for _ in range(10)]
    result = 0
    for row in range(N):
        for state in range(1 << M):
            if not check(row, state):
                continue
            for _state in range(1 << M):
                if not check(row-1, _state):
                    continue
                count = 0
                ok = True
                for j in range(M):
                    if isOn(state, j):
                        count += 1
                        if (j - 1 >= 0 and isOn(_state, j-1)) or (j + 1 < M and isOn(_state, j+1)):
                            ok = False
                if ok:
                    DP[row][state] = max(
                        DP[row][state], (DP[row-1][_state]) * (row != 0) + count)
            result = max(DP[row][state], result)
    print(result)

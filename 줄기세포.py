import sys
import pprint
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # max값 찾기
    Max = 0
    for i in range(N):
        Max = max(Max, max(board[i]))
    print(Max)
    # 큰 배열 만들어주고, 배열의 첫부분을 같이 기록해준다. 그리고 턴을 기록해준다
    turn = 0
    Board = [[[] for x in range(350)] for y in range(3500)]

    for y in range(150,150+N):
        for x in range(150,150+M):
            print(Board[y][x], end=' ')
        print()
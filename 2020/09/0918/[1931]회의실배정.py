import sys
sys.stdin = open('1931.txt', 'r')

N = int(input())
ROOM = [list(map(int, input().split())) for _ in range(N)]
print(ROOM)

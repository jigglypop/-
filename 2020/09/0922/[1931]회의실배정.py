import sys
sys.stdin = open('1931.txt', 'r')

N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]
rooms = sorted(rooms, key=lambda x: x[0])
rooms = sorted(rooms, key=lambda x: x[1])

result = 0
start = 0
for room in rooms:
    if room[0] >= start:
        start = room[1]
        result += 1
print(result)

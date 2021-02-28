import sys
sys.stdin = open('7568.txt', 'r')
input = sys.stdin.readline
N = int(input())
peoples = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    result = 1
    for j in range(N):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            result += 1
    print(result, end=' ')

import sys
sys.stdin = open('1946.txt', 'r')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    peoples = [list(map(int, input().split())) for _ in range(N)]
    peoples.sort()
    print(peoples)

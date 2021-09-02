import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("5676.txt", "r")
input = sys.stdin.readline
while True:
    start = input()
    if not start:
        break
    N, K = map(int, start.split())
    nums = list(map(int, input().split()))
    for _ in range(K):
        temp = list(input().split())

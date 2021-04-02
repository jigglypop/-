import sys
sys.stdin = open("2291.txt", "r")
input = sys.stdin.readline
N, M, K = map(int, input().split())
print(N, M, K)

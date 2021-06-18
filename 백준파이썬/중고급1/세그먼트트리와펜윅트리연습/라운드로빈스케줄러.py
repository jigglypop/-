import sys
sys.stdin = open("12016.txt", "r")
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
print(N, nums)

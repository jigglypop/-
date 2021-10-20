import sys
sys.stdin = open("./text/17952.txt", "r")
N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    print(nums)
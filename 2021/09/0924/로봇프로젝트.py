import sys
sys.stdin = open('./text/3949.txt', 'r')
for _ in range(int(input())):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    nums.sort()
    print(nums)

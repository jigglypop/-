from itertools import permutations
import sys
sys.stdin = open("./text/15649.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M = Split()
nums = [i for i in range(1, N + 1)]
for num in list(permutations(nums, M)):
    print(*num)
import sys
from collections import deque
sys.stdin = open("2659.txt", "r")
nums = deque(map(int, input().split()))
num_list = []
for i in range(4):
    num_list.append(int(''.join(list(map(str, nums)))))
    nums.rotate(1)
print(min(num_list) - 1112)

import sys
sys.stdin = open("./2491.txt", "r")
input = sys.stdin.readline
MAX = sys.maxsize
N = int(input()) 
nums = list(map(int, input().split()))
dpMin = [1] * (N + 1)
dpMax = [1] * (N + 1)
for i in range(1, N):
    if nums[i] > nums[i - 1]:
        dpMax[i] = dpMax[i - 1] + 1
        dpMin[i] = 1
    elif nums[i] < nums[i - 1]:
        dpMin[i] = dpMin[i - 1] + 1
        dpMax[i] = 1
    else:
        dpMin[i] = dpMin[i - 1] + 1
        dpMax[i] = dpMax[i - 1] + 1
print(max(max(dpMin), max(dpMax)))

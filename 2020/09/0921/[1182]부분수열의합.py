import sys
from pprint import pprint
from copy import deepcopy
sys.stdin = open('1182.txt', 'r')

N, S = map(int, input().split())
nums = list(map(int, input().split()))
results = []


def subset(index, chosen):
    results.append(chosen)
    for i in range(index, len(nums)):
        subset(i+1, chosen + [nums[i]])


subset(0, [])
count = 0
for result in results:
    if result and sum(result) == S:
        count += 1

print(count)

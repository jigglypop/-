import sys
from math import ceil
sys.stdin = open("./text/1475.txt", "r")
input = sys.stdin.readline
nums = list(input())
num_obj = {}
for str_num in nums:
    num = int(str_num)
    if num not in num_obj:
        num_obj[num] = 1
    else:
        num_obj[num] += 1
nine = num_obj[9] if 9 in num_obj else 0
six = num_obj[6] if 6 in num_obj else 0
half = ceil((nine + six) / 2)
num_obj[9] = half
num_obj[6] = half
Max = 0
for v in num_obj.values():
    Max = max(Max, v)
print(Max)
import sys
import re
sys.stdin = open('1541.txt', 'r')
input = sys.stdin.readline
A = str(input())
calc = list(re.findall('\+|-', A))
nums = list(map(int, re.split('\+|-', A)))
result = nums[0]
flag = True
for i in range(len(calc)):
    if flag:
        if calc[i] == '+':
            result += nums[i+1]
        else:
            result -= nums[i+1]
            flag = False
    else:
        result -= nums[i+1]
print(result)

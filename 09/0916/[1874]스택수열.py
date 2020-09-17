import sys
from collections import deque
sys.stdin = open('1874.txt', 'r')

N = int(input())
count = 0
stack = []
result = []
NO = ""

for _ in range(N):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        NO = 'NO'
        exit(0)
if NO:
    print(NO)
else:
    for r in result:
        print(r)

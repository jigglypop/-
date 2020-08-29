import sys
from collections import deque
sys.stdin = open("8111.txt", 'r')

T = int(input())
for _ in range(T):
    N = int(input())
    Q = deque(['1'])
    result = 'BRAK'
    while Q:
        num = int(Q.popleft())
        print(num)
        if num % N == 0:
            result = str(num)
            break
        else:
            Q.append(str(num) + '1')
            Q.append(str(num) + '0')
    print(result)

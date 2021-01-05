import sys
from collections import deque
sys.stdin = open('5430.txt', 'r')


def isvalid(orders, string):
    front = True
    if string[0] != '':
        Q = deque(string)
    else:
        return 'error'
    for order in orders:
        if order == 'R':
            front = not front
        elif order == 'D':
            if len(Q) == 0:
                return 'error'
            elif front:
                Q.popleft()
            else:
                Q.pop()
    return '[' + ','.join(list(Q)) + ']' if front else '[' + ','.join(reversed(list(Q))) + ']'


for _ in range(int(input())):
    orders = list(input())
    N = int(input())
    string = input().strip('[]').split(',')
    print(isvalid(orders, string))

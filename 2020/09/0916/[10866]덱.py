import sys
from collections import deque
sys.stdin = open('10866.txt', 'r')

orders = [list(map(str, input().split())) for _ in range(int(input()))]
Deque = deque()
for order in orders:
    if order[0] == 'push_front':
        Deque.appendleft(order[1])
    elif order[0] == 'push_back':
        Deque.append(order[1])
    elif order[0] == 'pop_front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.popleft())
    elif order[0] == 'pop_back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())
    elif order[0] == 'size':
        print(len(Deque))
    elif order[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    else:
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])

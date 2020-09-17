import sys
from collections import deque
sys.stdin = open('18258.txt', 'r')

N = int(input())
order = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

q = deque()
count = 0
for i in range(len(order)):
    if order[i][0] == "push":
        q.append(int(order[i][1]))
        count += 1
    elif order[i][0] == "pop":
        if count == 0:
            print(-1)
        else:
            print(q.popleft())
            count -= 1
    elif order[i][0] == "size":
        print(count)
    elif order[i][0] == "empty":
        if count == 0:
            print(1)
        else:
            print(0)
    elif order[i][0] == "front":
        if count == 0:
            print(-1)
        else:
            print(q[0])
    elif order[i][0] == "back":
        if count == 0:
            print(-1)
        else:
            print(q[len(q) - 1])

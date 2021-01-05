import sys
import heapq
from pprint import pprint
sys.stdin = open("틱택토.txt", 'r')


def xprint(m):
    for i in m:
        print(i)


m = []
while 1:
    a = input()
    if a == 'end':
        break
    m.append(list(a))
for tc in range(len(m)):
    ticktackto = [m[tc][:3], m[tc][4:7], m[tc][6:]]
    xprint(ticktackto)
    print('------')

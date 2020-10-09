import sys
from collections import defaultdict
sys.stdin = open('16936.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
temp = defaultdict(list)
for a in A:
    i = 0
    temp_a = 3
    while True:
        if a % temp_a != 0:
            print(a)
            break
        temp_a *= 3
        i += 1
    temp[i].append(a)
values = sorted(list(temp.items()), reverse=True)
for value in values:
    print(*(sorted(value[1])), end=' ')

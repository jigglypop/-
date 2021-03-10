import itertools
import sys
sys.stdin = open("3048.txt", "r")

N1, N2 = map(int, input().split())
group1 = list(' '.join(list(input()[::-1])))
group2 = list(' '.join(list(input())))
T = int(input())

group2 = [' ']*len(group1)+group2+[' ']*len(group1)
group1 = [' ']*T*2+group1

for a in itertools.zip_longest(group1, group2, fillvalue=' '):
    a = ''.join(a).strip()
    if a:
        print(a, end='')

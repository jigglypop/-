import sys
from collections import Counter
sys.stdin = open('[백준10816]숫자카드2.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
counter = Counter(A)
for i in m:
    print(counter[i], end=" ")

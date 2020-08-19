import sys
import collections
sys.stdin = open('2490.txt', 'r')


for _ in range(3):
    m = list(map(int, input().split()))
    yut = {1: 'A', 2: "B", 3: "C", 4: "D", 0: "E"}
    M = collections.Counter(m)
    print(yut[M[0]])

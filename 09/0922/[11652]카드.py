import sys
from collections import Counter
sys.stdin = open('11652.txt', 'r')

N = int(input())
board = [int(input()) for _ in range(N)]
counter = Counter(board)
count = []
for key, value in counter.items():
    count.append((value, key))
count = sorted(count, key=lambda x: (-x[0], x[1]))
print(count[0][1])

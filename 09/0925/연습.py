import sys
from bisect import bisect_left
from collections import Counter, defaultdict
sys.stdin = open('14003.txt', 'r')
input = sys.stdin.readline
A = [4, 5, 6, 5, 4, 3]
A = Counter(A)
B = []
for key, value in A.items():
    B.append((value, key))
B = sorted(B)
result = []
for key, value in B:
    result.extend([value]*key)
print(result)

import sys
from collections import defaultdict
from math import log10
sys.stdin = open('1339.txt', 'r')

count = 0
N = 1
logN = int(log10(N))+1
for i in range(1, logN+1):
    Max = min(10**i-1, N)
    Min = 10**(i-1) - 1
    count += (Max - Min) * i

print(count)

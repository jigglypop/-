import sys
import collections
sys.stdin = open('10797.txt', 'r')

N = int(input())
m = list(map(int, input().split()))
M_dict = collections.Counter(m)
print(M_dict[N])

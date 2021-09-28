from pprint import pprint
import sys
sys.stdin = open('./text/1654.txt', 'r')
input = sys.stdin.readline
K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
lo, hi = 1, max(lans) + 1

def lan(x):
    return sum([lan // x for lan in lans])
    
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if lan(mid) >= N:
        lo = mid
    else:
        hi = mid
print(lo)
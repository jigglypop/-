import sys
sys.stdin = open('./text/1557.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

K = Int()
print(K)
lo, hi = 2, 31623
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if mid ** 2 - (mid - 2) < K:
        lo = mid 
    else:
        hi = mid 
print(lo, hi)

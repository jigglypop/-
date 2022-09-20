import sys
sys.stdin = open('./text/1182.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
N, S = Split()
nums = List()
count = 0
for i in range(1, 1 << N):
    _S = 0
    for j in range(N):
        if i & (1 << j):
            _S += nums[j]
    if _S == S :
        count += 1
print(count)
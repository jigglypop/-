import sys
sys.stdin = open('./text/1557.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def Float():return float(input().strip())

MAX = 50000
K = Int()
board = [0] * (MAX + 1)

def nono(k):
    count = 0
    for i in range(1, k + 1):
        if i ** 2 > k:
            break
        count += board[i] * (k // i ** 2)
    return count

board[1] = 1
for i in range(1, MAX):
    for j in range(2 * i, MAX + 1, i):
        board[j] -= board[i]

l, r = 0, MAX ** 2 -1
while l!=r:
    m = (l + r) // 2
    if nono(m) >= K:
        r = m
    else:
        l = m + 1
print(l)
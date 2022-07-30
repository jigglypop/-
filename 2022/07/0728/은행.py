import sys
sys.stdin = open('./text/10350.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
board = List()
count = 0
Sum = sum(board)
for i in range(N):
    temp = board[i]
    if temp < 0: count += -(temp + 1) // Sum + 1
    j = (i + 1) % N
    while i != j:
        temp += board[j]
        if temp < 0: count += -(temp + 1) // Sum + 1
        j = (j + 1) % N
print(count)
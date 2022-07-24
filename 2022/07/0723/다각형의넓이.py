import sys
sys.stdin = open('./text/2166.txt', 'r')
input = sys.stdin.readline
def Split():return map(float, input().strip().split())
def List():return list(map(float, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
x, y = [], []
result = 0
for _ in range(N):
    a, b = Split()
    x.append(a)
    y.append(b)
x, y = x + [x[0]], y + [y[0]]
for i in range(N):
    result += (x[i] * y[i + 1]) - (x[i + 1] * y[i])
print(round(abs(result)/2, 1))
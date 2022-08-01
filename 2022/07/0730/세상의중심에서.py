from math import sqrt
import sys
sys.stdin = open('./text/2389.txt', 'r')
input = sys.stdin.readline
def Split():return map(float, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def enclosing_sphere(x, y):
    n = len(x)
    X, Y = 0, 0
    for i in range(n):
        X += x[i]
        Y += y[i]
    X /= n
    Y /= n
    r = 0.1
    for i in range(10000):
        maxV = -1
        maxP = -1
        for j in range(n):
            temp = (x[j] - X) ** 2 + (y[j] - Y) ** 2
            if maxV < temp:
                maxV = temp
                maxP = j
        X += (x[maxP] - X) * r
        Y += (y[maxP] - Y) * r
        r *= 0.998
    return round(X, 3), round(Y, 3), round(maxV ** 0.5, 3)

N = Int()
x, y = [], []
for _ in range(N):
    a, b = Split()
    x.append(a)
    y.append(b)
print(*enclosing_sphere(x, y))
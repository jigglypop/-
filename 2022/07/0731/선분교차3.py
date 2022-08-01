import sys
sys.stdin = open('./text/1298.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

x1, y1, x2, y2 = Split()
x3, y3, x4, y4 = Split()

a, b, c, d = [x1,y1],[x2,y2],[x3,y3],[x4,y4]

def ccw(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])

L = ccw(a,b,c) * ccw(a,b,d)
R = ccw(c,d,a) * ccw(c,d,b)
if L <= 0 and R <= 0:
    if L == 0 and R == 0:
        if max(a[0],b[0]) >= min(c[0],d[0]) and max(c[0],d[0]) >= min(a[0],b[0]) and max(a[1],b[1]) >= min(c[1],d[1]) and max(c[1],d[1]) >= min(a[1],b[1]):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
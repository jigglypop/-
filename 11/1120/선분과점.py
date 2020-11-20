import sys
sys.stdin = open('11664.txt', 'r')


def dist(x1, y1, z1, x2, y2, z2):
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5


x1, y1, z1, x2, y2, z2, x3, y3, z3 = map(int, input().split())


def inpoint(p):
    dx, dy, dz = x2-x1, y2-y1, z2-z1
    return x1+p*dx, y1+p*dy, z1+p*dz


left = 0
right = 1
ans = 10**12
while abs(left-right) > 1e-12:
    p1 = (2*left + right)/3
    p2 = (left + 2*right)/3
    d1 = dist(x3, y3, z3, *inpoint(p1))
    d2 = dist(x3, y3, z3, *inpoint(p2))
    ans = min(ans, d1, d2)
    if d1 < d2:
        right = p2
    else:
        left = p1
print(round(ans, 10))

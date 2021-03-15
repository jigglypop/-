import sys
sys.stdin = open("14719.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
H = list(map(int, input().split()))
V = 0
l, r = 0, X - 1
L, R = H[l], H[r]
while l < r:
    L, R = max(H[l], L), max(H[r], R)
    if L <= R:
        V += L - H[l]
        l += 1
    else:
        V += R - H[r]
        r -= 1
print(V)

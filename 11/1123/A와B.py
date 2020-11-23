import sys
sys.stdin = open('12904.txt', 'r')
S = list(input())
T = list(input())

while len(T) > len(S):
    q = T.pop()
    if q == 'B':
        T = T[::-1]
print(1) if S == T else print(0)

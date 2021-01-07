import sys
sys.stdin = open('10799.txt', 'r')
input = sys.stdin.readline
stick = list(input())
result = 0
S = []
for i in range(len(stick)):
    if stick[i] == '(':
        S.append('(')
    else:
        if stick[i-1] == '(':
            S.pop()
            result += len(S)
        else:
            S.pop()
            result += 1
print(result)

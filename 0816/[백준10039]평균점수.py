import sys
sys.stdin = open('[백준10039]평균점수.txt', 'r')

M = [int(input()) for _ in range(5)]
for i in range(len(M)):
    if M[i] < 40:
        M[i] = 40

print(sum(M)//len(M))

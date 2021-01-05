import sys

sys.stdin = open('10989.txt', 'r')
N = int(input())
dic = {}
for i in range(N):
    a = int(sys.stdin.readline())
    if a in dic:
        dic[a] = dic[a] + 1
    else:
        dic[a] = 1
for sorted in sorted(dic.items()):
    for i in range(sorted[1]):
        print(sorted[0])

import sys
sys.stdin = open('1152.txt', 'r')

print(len(list(map(str, input().split()))))

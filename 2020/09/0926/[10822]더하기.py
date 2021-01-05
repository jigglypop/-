import sys
sys.stdin = open('10822.txt', 'r')
print(sum(list(map(int, input().split(',')))))

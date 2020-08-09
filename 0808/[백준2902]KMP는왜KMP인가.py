import sys
sys.stdin = open('[백준2902]KMP는왜KMP인가.txt', 'r')
input = sys.stdin.readline

M = list(str(input()).split('-'))
for m in M:
    print(m[0], end='')

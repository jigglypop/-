import sys
sys.stdin = open('10842.txt', 'r')

input = sys.stdin.readline
A, B, C, D = map(str, input().split())
print(int(A+B) + int(C+D))

import sys
sys.stdin = open("./text/2525.txt", "r")
input = sys.stdin.readline
A, B = map(int, input().split())
C = int(input())
B += C
a, b = B // 60, B % 60
A += a
B = b
A %= 24
print(A, B)


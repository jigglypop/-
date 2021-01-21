import sys
sys.stdin = open("10430.txt", "r")
input = sys.stdin.readline

a, b, c = map(int, input().split())
print((a % c+b % c) % c)
print((a % c+b % c) % c)
print((a % c*b % c) % c)
print((a % c*b % c) % c)

import sys
sys.stdin = open('11953.txt', 'r')

for _ in range(int(input())):
    a, b = map(int, input().split(','))
    print(a+b)

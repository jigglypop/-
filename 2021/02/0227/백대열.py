import sys
sys.stdin = open('14490.txt', 'r')

a, b = list(map(int, input().split(':')))
n, m = a, b
while b > 0:
    a, b = b, a % b
print(f'{n // a}:{m // a}')

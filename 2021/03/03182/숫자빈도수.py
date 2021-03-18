import sys
sys.stdin = open("14912.txt", "r")
n, d = map(int, input().split())
print(''.join(map(str, range(1, n+1))).count(str(d)))

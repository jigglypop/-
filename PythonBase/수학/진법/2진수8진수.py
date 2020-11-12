import sys
sys.stdin = open("1373.txt", "r")
input = sys.stdin.readline

s = input()
n = len(s)
ans = ''
if n % 3 == 1:
    print(s[0], end='')
elif n % 3 == 2:
    print((ord(s[0])-ord('0'))*2 + ord(s[1])-ord('0'), end='')
for i in range(n % 3, n, 3):
    print((ord(s[i])-ord('0'))*4 + (ord(s[i+1])-ord('0'))
          * 2 + (ord(s[i+2])-ord('0')), end='')

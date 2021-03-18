import sys
sys.stdin = open("1254.txt", "r")
s = input()
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break

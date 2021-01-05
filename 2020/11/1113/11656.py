import sys
sys.stdin = open('11656.txt', 'r')

input = sys.stdin.readline
s = input()
n = len(s)
a = [s[i:] for i in range(n)]
a.sort()
print('\n'.join(a))

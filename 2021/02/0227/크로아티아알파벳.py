import sys
sys.stdin = open('2941.txt', 'r')
input = sys.stdin.readline
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for t in a:
    alpha = alpha.replace(t, '*')
    print(alpha)
print(len(alpha))

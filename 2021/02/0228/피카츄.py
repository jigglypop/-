import sys
sys.stdin = open('14405.txt', 'r')
t = input()
a, b, c = [t.count(_)for _ in['pi', 'ka', 'chu']]
print('YNEOS'[2*a+2*b+3*c < len(t)::2])

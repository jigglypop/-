import re
import sys
sys.stdin = open('16172.txt', 'r')
s = input()
k = input()
t = re.sub('[0-9]', '', s)
if k in t:
    print('1')
else:
    print('0')

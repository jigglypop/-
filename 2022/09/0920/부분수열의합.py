import sys
sys.stdin = open('./text/1182.txt', 'r')
input = sys.stdin.readline
def List():return list(map(str, input().strip().split()))
def Int():return int(input().strip())
S = 0b0
for _ in range(Int()):
    temp = List()
    if temp[0] == 'all':
        S = 0b111111111111111111111
    elif temp[0] == 'empty':
        S = 0
    elif temp[0] == 'add':
        S |= (0b1 << int(temp[1]))
    elif temp[0] == 'remove':
        S &= ~(0b1 << int(temp[1]))
    elif temp[0] == 'check':
        print(int(S & (0b1 << int(temp[1])) != 0))
    elif temp[0] == 'toggle':
        S ^= (0b1 << int(temp[1]))


import sys
sys.stdin = open('9012.txt', 'r')

N = int(input())
for _ in range(N):
    PS = list(input())
    stack = []
    for p in PS:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')

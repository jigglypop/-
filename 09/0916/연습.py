import sys
sys.stdin = open('1874.txt', 'r')

N = int(input())
stack = [0]
count = 1
ans = []
for _ in range(N):
    num = int(input())
    while stack[-1] < num:
        stack.append(count)
        count += 1
        ans += ['+']
    if stack[-1] == num:
        stack.pop(-1)
        ans += ['-']
    else:
        print("NO")
        exit(0)
else:
    print('\n'.join(ans))

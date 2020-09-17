from collections import deque
import sys
sys.stdin = open('1021.txt', 'r')
N, _ = map(int, input().split())
nums = list(map(int, input().split()))
Q = deque([i for i in range(1, N + 1)])
count = 0

for num in nums:
    if num == Q[0]:
        Q.popleft()
    else:
        left = Q.index(num)
        right = len(Q) - left
        if left <= right:
            Q.rotate(-left)
            Q.popleft()
            count += left
        else:
            Q.rotate(right)
            Q.popleft()
            count += right
print(count)

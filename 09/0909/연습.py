from collections import deque


Q = deque([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(Q)
Q.rotate(1)
print(Q)

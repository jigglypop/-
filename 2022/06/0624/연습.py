from bisect import *

tree = [0, 4, 2, 2, 2, 0, 2]

def query(l, r):
    result = 0
    while l <= r:
        if l % 2 == 1:
            result += tree[l]
            l += 1
        if r % 2 == 0:
            result += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return result

def update(n, diff):
    while n >= 1:
        tree[n] += diff
        n //= 2

print(query(4, 6))
update(5, 2)
print(query(4, 6))
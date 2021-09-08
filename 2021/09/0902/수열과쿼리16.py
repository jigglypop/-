import sys
sys.stdin = open('14428.txt', 'r')
N = int(input())
INF = sys.maxsize


def update(i, x):
    while i < len(tree):
        _i = tree[i]
        _x = nums[_i]
        if _x > x:
            print('1', _x, _i, x, i, tree)
            tree[i] = _i
        elif _x < x:
            print('2', _x, _i, x, i, tree)
            tree[i] = i
        else:
            print('3', _x, _i, x, i, tree)
            tree[i] = min(i, _i)
        i += (i & -i)


nums = [sys.maxsize] + list(map(int, input().split()))
tree = [i for i in range(N + 1)]

for i in range(1, len(nums)):
    update(i, nums[i])
print(tree)
for _ in range(int(input())):
    q, a, b = map(int, input().split())
    if q == 2:
        print('PRINT')
    else:
        i = a
        update(i, b - nums[b])

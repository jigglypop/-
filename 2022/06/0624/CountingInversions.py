import sys
sys.stdin = open("./text/10090.txt", "r")
input = sys.stdin.readline
N = int(input())
tree = [0] * (N + 2)
nums = list(map(int, input().strip().split()))

def update(i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)

def sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s

nums = sorted(list(enumerate(nums)), key=lambda x: x[1])
result = 0
for i, _ in nums:
    update(i + 1, 1)
    result += (sum(N + 1) - sum(i + 1))
print(result)

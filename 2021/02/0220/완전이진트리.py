import sys
sys.stdin = open("9934.txt", 'r')
K = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(K)]


def devide(nums, k):
    global tree
    if k == K:
        return
    root = len(nums) // 2
    tree[k].append(nums[root])
    devide(nums[:root], k+1)
    devide(nums[root+1:], k+1)


devide(nums, 0)
for t in tree:
    print(*t)

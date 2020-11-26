tree = [21, 10, 7, 5, 1]
visited = 10
idx = len(tree)
temp = 0
for i in range(len(tree)-1, -1, -1):
    temp += tree[i]
    idx -= 1
    if temp + tree[i] > visited:
        break
    tree[i] += 1
total = 0
for t in tree[:idx]:
    total += t // 2
print(tree)
print(tree[idx:])
print(idx)
print(total)

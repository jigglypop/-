import sys
sys.stdin = open("2116.txt", "r")
input = sys.stdin.readline
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
route = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
max_num = 0

for i in range(6):
    result = []
    temp = [1, 2, 3, 4, 5, 6]
    temp.remove(dice[0][i])
    next_ = dice[0][route[i]]
    temp.remove(next_)
    result.append(max(temp))
    for j in range(1, N):
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(next_)
        next_ = dice[j][route[dice[j].index(next_)]]
        temp.remove(next_)
        result.append(max(temp))
    result = sum(result)
    if max_num <= result:
        max_num = result
print(max_num)

import sys
from itertools import combinations_with_replacement
sys.stdin = open("./text/7490.txt")

def go(k, value, strs):
    if k == N - 1:
        if value == 0:
            result.append(strs)
        return
    calc_list = [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: int(str(x) + str(y))
    ]
    calc_str = ['+', '-', " "]
    for i in range(3):
        calc = calc_list[i]
        S = calc_str[i]
        temp = calc(value, nums[k + 1])
        go(k + 1, temp, strs + S + str(nums[k + 1]))

for _ in range(int(input())):
    N = int(input())
    nums = [i for i in range(1, N + 1)]
    calc_nums = [0, 1, 2, 3]
    result = []
    go(0, nums[0], '1')
    for r in result:
        print(r)
    print()

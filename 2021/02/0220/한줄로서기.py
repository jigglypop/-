import sys
sys.stdin = open("1138.txt", 'r')
K = int(input())
count = list(map(int, input().split()))
peoples = [i+1 for i in range(K)]
result = []


def solve(nums):
    for i in range(len(nums)):
        temp = 0
        for j in range(i):
            if nums[i] < nums[j]:
                temp += 1
        if count[nums[i]-1] != temp:
            return False
    return True


def comb(k, used, choice):
    global result
    if k == len(peoples):
        if solve(choice):
            result.append(choice[::])
        return
    for i in range(len(peoples)):
        if used & (1 << i):
            continue
        choice.append(peoples[i])
        comb(k+1, used | (1 << i), choice)
        choice.pop()


comb(0, 0, [])
print(*result[0])

import sys
sys.stdin = open('10819.txt', 'r')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
Max = -sys.maxsize


def perm(k, choice, used):
    global Max
    if k == N:
        temp = 0
        for i in range(N-1):
            temp += abs(choice[i] - choice[i+1])
        Max = max(Max, temp)
        return
    for i in range(N):
        if used & (1 << i):
            continue
        choice.append(nums[i])
        perm(k+1, choice, used | (1 << i))
        choice.pop()


perm(0, [], 0)
print(Max)

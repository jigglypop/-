import sys
sys.stdin = open('15658.txt', 'r')

N = int(input())
board = list(map(int, input().split()))
count = list(map(int, input().split()))
n = len(board)
Max = -sys.maxsize
Min = sys.maxsize


def calc(num, x, y):
    if num == 0:
        return x+y
    elif num == 1:
        return x-y
    elif num == 2:
        return x*y
    else:
        return x//y if x//y >= 0 else (x*-1)//y * -1


def perm(k, sums, count):
    global Max, Min
    if k == n:
        Max = max(Max, sums)
        Min = min(Min, sums)
        return
    for i in range(4):
        if count[i] == 0:
            continue
        count[i] -= 1
        temp = calc(i, sums, board[k])
        perm(k+1, temp, count)
        count[i] += 1


perm(1, board[0], count[::])
print(Max)
print(Min)

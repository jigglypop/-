import sys
sys.stdin = open('10815.txt', 'r')

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cards.sort()
for num in nums:
    start, end = 0, N-1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        temp = cards[mid]
        if num > temp:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    if cards[result] == num:
        print(1)
    else:
        print(0)

import sys
sys.stdin = open('10816.txt', 'r')


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
cards.sort()


def lower_bound(cards, num):
    start, end = 0, N-1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if num == cards[mid]:
            result = mid
            end = mid - 1
        elif num > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return result


def upper_bound(cards, num):
    start, end = 0, N-1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if num == cards[mid]:
            result = mid
            start = mid + 1
        elif num > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return result


for num in nums:
    r = upper_bound(cards, num)
    l = lower_bound(cards, num)
    result = 0 if l == -1 else r - l + 1
    print(result, end=' ')

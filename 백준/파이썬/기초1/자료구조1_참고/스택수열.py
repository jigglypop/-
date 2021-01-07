import sys
from pprint import pprint
sys.stdin = open('1874.txt', 'r')
N = int(input())
nums = [int(input()) for _ in range(N)]


def go():
    i = 1
    S = []
    result = []
    for num in nums:
        while i <= num:
            S.append(i)
            result.append('+')
            i += 1
        if S.pop() != num:
            print('NO')
            return
        else:
            result.append('-')
    for r in result:
        print(r)
    return


go()

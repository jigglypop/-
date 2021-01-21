import sys
sys.stdin = open('7795.txt', 'r')
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    answer = 0
    for temp in A:
        start = 0
        end = b - 1
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if B[mid] < temp:
                result = mid
                start = mid + 1
            else:
                end = mid - 1
        if B[result] < temp:
            answer += result + 1
        else:
            answer += result
    print(answer)

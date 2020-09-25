import sys
sys.stdin = open('2343.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))
start = max(lessons)
end = sum(lessons)
result = end
while start <= end:
    mid = (start + end) // 2
    count = 1
    temp = 0
    for lesson in lessons:
        temp += lesson
        if temp > mid:
            temp = lesson
            count += 1
    if count <= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)

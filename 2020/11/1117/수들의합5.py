import sys
sys.stdin = open('2018.txt', 'r')
input = sys.stdin.readline
N = int(input())
left = right = Sum = result = 0
while True:
    if Sum >= N:
        Sum -= left + 1
        left += 1
    elif right == N:
        break
    else:
        Sum += right + 1
        right += 1
    if Sum == N:
        result += 1
print(result)

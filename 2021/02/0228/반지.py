import sys
sys.stdin = open('5555.txt', 'r')

target = input()
N = int(input())

result = 0
for _ in range(N):
    word = input()
    word = word + word + word
    if word.count(target) >= 1:
        result += 1
print(result)

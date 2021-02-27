import sys
sys.stdin = open('5525.txt', 'r')
N = int(input())
M = int(input())
string = input()
index = 1
answer = 0
pattern = 0
while index < M-1:
    if string[index-1] == 'I' and string[index] == 'O' and string[index+1] == 'I':
        pattern += 1
        if pattern == N:
            answer += 1
            pattern -= 1
        index += 1
    else:
        pattern = 0
    index += 1
print(answer)

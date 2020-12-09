import sys
from collections import deque
sys.stdin = open('17413.txt', 'r')
input = sys.stdin.readline
words = input().split('<')
result = ''
for word in words:
    if '>' in word:
        temp = word.split('>')
        result += '<' + temp[0]+">" + \
            " ".join(map(lambda x: x[::-1], temp[1].split()))
    else:
        result += ' '.join(map(lambda x: x[::-1], word.split()))
print(result)

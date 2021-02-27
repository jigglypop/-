import sys
import re
from collections import Counter
sys.stdin = open('1316.txt', 'r')
N = int(input())
result = 0
for _ in range(N):
    stack = []
    words = input()
    word_counter = Counter(words)
    flag = True
    for key, value in word_counter.items():
        temp = re.findall(f"{key}+", words)
        if len(temp) >= 2:
            flag = False
            break
    if flag:
        result += 1
print(result)

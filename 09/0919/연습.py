import sys
from collections import defaultdict
sys.stdin = open('1339.txt', 'r')

digit = defaultdict(int)
for _ in range(int(input())):
    i = 0
    for word in input()[::-1]:
        digit[word] += 10**i
        i += 1
result = 0
j = 9
for n in sorted(digit.values(), reverse=True):
    result += n * j
    j -= 1
print(result)

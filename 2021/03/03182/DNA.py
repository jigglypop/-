import sys
from collections import Counter
sys.stdin = open("1969.txt", "r")
N, M = map(int, input().split())
DNAs = [list(input()) for _ in range(N)]
result = 0
result_word = ''
for x in range(M):
    X = [DNAs[i][x] for i in range(N)]
    counter = Counter(X)
    temp = []
    for word, count in counter.items():
        temp.append((count, -ord(word), word))
    temp.sort(reverse=True)
    count, _, alpha = temp[0]
    result += N - count
    result_word += alpha

print(result_word)
print(result)

import sys
sys.stdin = open('1181.txt', 'r')

N = int(input())
board = [input() for _ in range(N)]
words = []
for b in board:
    words.append((len(b), b))
words = sorted(list(set(words)), key=lambda x: (x[0], x[1]))
for word in words:
    print(word[1])

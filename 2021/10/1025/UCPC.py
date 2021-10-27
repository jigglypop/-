import sys
sys.stdin = open("./15904.txt", "r")
boards = list(map(str, input().split()))
words = ""
for board in boards:
    words += board[0]
print(words)
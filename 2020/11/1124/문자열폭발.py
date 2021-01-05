import sys
sys.stdin = open('9935.txt', 'r')
input = sys.stdin.readline
words = input()
bomb = input()
last = bomb[-1]
S = []
for word in words:
    S.append(word)
    if word == last and ''.join(S[-len(bomb):]) == bomb:
        del S[-len(bomb):]
print(''.join(S)) if len(S) != 0 else print("FRULA")

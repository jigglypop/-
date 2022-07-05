import sys
sys.stdin = open("./text/1918.txt", "r")
input = sys.stdin.readline
words = input().strip()
Op = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
postfix = []
S = []
for word in words:
    if 'A' <= word<= 'Z':
        postfix.append(word)
    elif word== '(':
        S.append(word)
    elif word== ')':
        while S and S[-1] != '(':
            postfix.append(S.pop())
        S.pop()
    else:
        while S and Op[word] <= Op[S[-1]]:
            postfix.append(S.pop())
        S.append(word)
postfix += S[::-1]
print("".join(postfix))
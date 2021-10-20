import sys
sys.stdin = open("./text/11899.txt", "r")
words = input()
count = 0
S = []
for word in words:
    if not S:
        if word == ')':
            count += 1
        else:
            S.append('(')
    else:
        if S[-1] == '(' and word == ')':
            S.pop()
        else:
            S.append(word)
print(count + len(S))
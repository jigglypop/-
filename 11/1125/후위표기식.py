import sys
sys.stdin = open('1918.txt', 'r')
input = sys.stdin.readline
a = ""
s = []
r = {"+": 2, "-": 2, "*": 3, "/": 3, "(": 0, ")": 1}
for i in input():
    if i in r:
        while s and r[i]:
            if s[-1] == "(":
                if i == ")":
                    s.pop()
                break
            elif r[s[-1]] >= r[i]:
                a += s.pop()
            else:
                break
        if i != ")":
            s += i
    else:
        a += i
print(a+"".join(reversed(s)))

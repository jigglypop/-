import sys
sys.stdin = open("1701.txt", "r")
input = sys.stdin.readline


def preprocessing(P):
    pi = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j-1]
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    return max(pi)


P = input()
ans = 0
for i in range(len(P)):
    ans = max(ans, preprocessing(P[i:len(P)]))

print(ans)

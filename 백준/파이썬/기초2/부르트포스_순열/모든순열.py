import sys
sys.stdin = open('10974.txt', 'r')
N = int(input())


def perm(k, choice, used):
    if k == N:
        for c in choice:
            print(c+1, end=' ')
        print()
        return
    for i in range(N):
        if used & (1 << i):
            continue
        choice.append(i)
        perm(k+1, choice, used | (1 << i))
        choice.pop()


perm(0, [], 0)

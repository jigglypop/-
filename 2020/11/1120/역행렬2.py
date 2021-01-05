import sys
sys.stdin = open('9254.txt', 'r')

input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[0 if x != y else 1 for x in range(N)] for y in range(N)]


def delete(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(A):
    for i in range(N):
        if A[i][i] == 0:
            for j in range(i+1, N):
                if A[i][j] != 0:
                    A[i], A[j] = A[j], A[i]
                    break
            else:
                print('no inverse')
                return -1
        for j in range(i+1, N):
            delete(A[i], A[j], i)
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            delete(A[i], A[j], i)
    for i in range(N):
        delete(A[i], A[i], i, target=1)
    return A


def inverse(A):
    tmp = [[] for _ in A]
    for i, row in enumerate(A):
        assert len(row) == N
        tmp[i].extend(row + [0] * i + [1] + [0]*(N-i-1))
    if gauss(tmp) == -1:
        return
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    [print(' '.join(map(str, row))) for row in ret]
    return


inverse(A)

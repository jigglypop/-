import sys
sys.stdin = open("16935.txt", "r")


def MAP():
    return map(int, input().split())


Y, X, r = MAP()
A = [list(MAP()) for _ in range(Y)]
for order in MAP():
    if order == 1:
        A = A[::-1]
    elif order == 2:
        A = [a[::-1] for a in A]
    elif order == 3:
        A = [[A[~y][x] for y in range(Y)] for x in range(X)]
        Y, X = X, Y
    elif order == 4:
        A = [[A[y][~x] for y in range(Y)] for x in range(X)]
        Y, X = X, Y
    elif order == 5:
        Y_, X_ = Y//2, X//2
        for y in range(Y_):
            for x in range(X_):
                A[y][x], A[y+Y_][x], A[y][x+X_], A[y+Y_][x+X_] =\
                    A[y+Y_][x], A[y+Y_][x+X_], A[y][x], A[y][x+X_]
    elif order == 6:
        Y_, X_ = Y//2, X//2
        for y in range(Y_):
            for x in range(X_):
                A[y][x], A[y+Y_][x], A[y][x+X_], A[y+Y_][x+X_] =\
                    A[y][x+X_], A[y][x], A[y+Y_][x+X_], A[y+Y_][x]

list(map(lambda a: print(*a), A))

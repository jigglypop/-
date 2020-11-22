import sys
sys.stdin = open('9254.txt', 'r')

input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def inverse(m, size):
    a = 0
    det = 1
    k = 0
    inv = [[1 if x == y else 0 for x in range(size)] for y in range(size)]
    for k in range(len(m)):
        if m[k][k] == 0:
            m = m[k+1:len(m)] + m[k:k+1]
            inv = inv[k+1:len(inv)] + inv[k:k+1]
            continue
        else:
            if m[k][k] == 1:
                for i in range(k+1, len(m)):
                    a = -m[i][k]
                    for j in range(len(m)):
                        if a == 0:
                            break
                        m[i][j] = a * m[k][j] + m[i][j]
                        inv[i][j] = a * inv[k][j] + inv[i][j]
            else:
                a = 1 / m[k][k]
                for i in range(len(m)):
                    m[k][i] = m[k][i] * a
                    inv[k][i] = inv[k][i] * a
                for i in range(k+1, len(m)):
                    a = -m[i][k]
                    for j in range(len(m)):
                        if a == 0:
                            break
                        m[i][j] = a * m[k][j] + m[i][j]
                        inv[i][j] = a * inv[k][j] + inv[i][j]
    for i in range(len(m)):
        det *= m[i][i]
    if det == 0:
        print('no inverse')
        return
    else:
        for k in range(len(m)-1, -1, -1):
            for i in range(k-1, -1, -1):
                a = -m[i][k]
                for j in range(len(m)-1, -1, -1):
                    if a == 0:
                        break
                    m[i][j] = a * m[k][j] + m[i][j]
                    inv[i][j] = a * inv[k][j] + inv[i][j]
        for i in inv:
            print(*i)
        return


inverse(A, N)

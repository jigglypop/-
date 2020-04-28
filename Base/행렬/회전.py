def rotate(m):
    N = len(m)
    A = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            A[x][N-1-y] = m[y][x]
    B = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            B[N-1-y][N-1-x] = m[y][x]
    C = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            C[N-1-x][y] = m[y][x]
    result = [A, B, C]
    return result
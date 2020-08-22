from queue import deque


def solution(board, movies):
    answer = 0
    N = len(board)
    M = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            M[y][x] = board[N-1-x][y]
    M_ = []
    for m in M:
        m_ = []
        for i in m:
            if i == 0:
                continue
            m_.append(i)
        M_.append(deque(m_))

    movies = [i-1 for i in movies]
    Q = []
    answer = 0
    for num in movies:
        if len(Q) == 0 and len(M_[num]) != 0:
            temp = M_[num].pop()
            Q.append(temp)
        elif len(M_[num]) == 0:
            continue
        else:
            if M_[num][-1] == Q[-1]:
                M_[num].pop()
                Q.pop()
                answer += 2
            else:
                temp = M_[num].pop()
                Q.append(temp)

    return answer

from pprint import pprint


def solution(n, build_frame):
    board_col = [[2]*n for _ in range(n)]
    board_beam = [[2]*n for _ in range(n)]

    for build in build_frame:
        x, y, col_beam, make_del = build
        if col_beam == 0:
            board_col[y-1][x-1] = 0
        else:
            board_beam[y-1][x-1] = 1
    pprint(board_beam)
    pprint(board_col)
    answer = [[]]

    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
      2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
#       1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

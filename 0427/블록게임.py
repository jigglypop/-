import numpy as np


def solution(board):
    answer = 0

    blocks = {}
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col > 0:
                if col not in blocks:
                    blocks[col] = {"left": 51, "right": -1,
                                   "top": 51, "bottom": -1, "coords": []}
                blocks[col]["left"] = min(blocks[col]["left"], j)
                blocks[col]["right"] = max(blocks[col]["right"], j)
                blocks[col]["top"] = min(blocks[col]["top"], i)
                blocks[col]["bottom"] = max(blocks[col]["bottom"], i)
                blocks[col]["coords"].append([i, j])
    board = np.array(board)
    removed = 1
    while removed > 0:
        removed = 0
        for block_key in blocks:
            can_remove = True
            block = blocks[block_key]
            zeros = 0
            for i in range(block["top"], block["bottom"]+1):
                for j in range(block["left"], block["right"]+1):
                    if board[i][j] == 0:
                        zeros += 1
                        if (board[:i, j] > 0).any():
                            can_remove = False
                            break
                if not can_remove:
                    break
            if can_remove and zeros == 2:
                for coord in blocks[block_key]["coords"]:
                    board[coord[0]][coord[1]] = 0
                del blocks[block_key]
                removed += 1
                answer += 1
                break
    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
    0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

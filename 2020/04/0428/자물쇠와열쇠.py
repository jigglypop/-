from pprint import pprint
import numpy as np


def white_black(lock, N_lock, pad):
    white_set = []
    black_set = []
    for y in range(N_lock):
        for x in range(N_lock):
            if lock[y][x] == 0:
                white_set.append((y+pad, x+pad))
            else:
                black_set.append((y+pad, x+pad))
    return set(white_set), set(black_set)


def solution(key, lock):
    N_key = len(key)
    N_lock = len(lock)
    pad = N_key-1

    white_lock, black_lock = white_black(lock, N_lock, pad)
    key = np.array(key)
    black_key_set = []
    for i in range(4):
        key = np.rot90(key)
        temp = []
        for y in range(N_key):
            for x in range(N_key):
                if key[y][x] == 1:
                    temp.append((y, x))
        black_key_set.append(temp)
    answer = False
    move_length = pad + N_lock
    for dy in range(move_length):
        for dx in range(move_length):

            for black_key in black_key_set:
                black_temp = []
                for y, x in black_key:
                    black_temp.append((y+dy, x+dx))
                black_temp = set(black_temp)
                if white_lock == black_temp.intersection(white_lock) and not black_lock & black_temp:
                    answer = True
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

import json
import requests
import math
import os
import random
import re
import sys
from pprint import pprint
from collections import deque


arr = 'ABC'
result = []

# 배열조작

# board = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# y = 1
# x = 1
# #  -1,-1   -1, 0    -1,1
# #   0,-1    0, 0     0,1
# #   1,-1    1, 0     1,1
# di = [(-1, -1), (-1, 0), (-1, 1),
#       (0, -1), (0, 0), (0, 1),
#       (1, -1), (1, 0), (1, 1)]
# # 북서 -1, -1
# ny, nx = y + di[0][0], x + di[0][1]
# print(board[ny][nx])
# # 위 -1, 0
# ny, nx = y + di[1][0], x + di[1][1]
# print(board[ny][nx])
# # 북동 -1, 1
# ny, nx = y + di[2][0], x + di[2][1]
# print(board[ny][nx])
# # 서 0, -1
# ny, nx = y + di[3][0], x + di[3][1]
# print(board[ny][nx])
# # 가운데 0, 0
# ny, nx = y + di[4][0], x + di[4][1]
# print(board[ny][nx])
# # 동 0, 1
# ny, nx = y + di[5][0], x + di[5][1]
# print(board[ny][nx])
# # 남서 1, -1
# ny, nx = y + di[6][0], x + di[6][1]
# print(board[ny][nx])
# # 아래 1, 0
# ny, nx = y + di[7][0], x + di[7][1]
# print(board[ny][nx])
# # 남동 1, 1
# ny, nx = y + di[8][0], x + di[8][1]
# print(board[ny][nx])


# 투포인터

# left = right = 0
# Sum = A[0]
# result = 0
# while left <= right and right < N:
#     if Sum < M:
#         right += 1
#         if right < N:
#             Sum += A[right]
#     elif Sum == M:
#         result += 1
#         right += 1
#         if right < N:
#             Sum += A[right]
#     elif Sum > M:
#         Sum -= A[left]
#         left += 1
#         if left > right and left < N:
#             right = left
#             Sum = A[left]

# 부분집합


# def subset(k):
#     N = len(arr)
#     for i in range(1 << N):
#         temp = []
#         for j in range(N):
#             if i & (1 << j):
#                 continue
#             temp.append(arr[j])
#         result.append(temp)


# 순열


# 조합

# def comb(k, chosen, start, r):
#     if k == r:
#         result.append(chosen[::])
#         return
#     for i in range(start, len(arr)):
#         chosen.append(arr[i])
#         comb(k+1, chosen, i+1)
#         chosen.pop()

# nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]

# lower_bound

# start, end = 0, N-1
# result = 0
# while start <= end:
#     mid = (start + end) // 2
#     temp = nums[mid]
#     # 여기
#     if temp < M:
#         start = mid + 1
#     else:
#         # 여기
#         result = mid
#         end = mid - 1

# upper_bound

# start, end = 0, N-1
# result = 0
# while start <= end:
#     mid = (start + end) // 2
#     temp = nums[mid]
#     # 여기
#     if temp <= M:
#         start = mid + 1
#     else:
#         # 여기
#         result = mid
#         end = mid - 1

# 정수

# import math

# x, y, c = 30, 40, 10
# left, right = 0, min(x, y)
# while(abs(right-left) > 1e-6):
#     mid = (left+right)/2.0
#     d = mid
#     h1 = math.sqrt(x*x-d*d)
#     h2 = math.sqrt(y*y-d*d)
#     h = (h1*h2)/(h1+h2)
#     if h > c:
#         left = mid
#     else:
#         right = mid


# 모듈

# from bisect import bisect_left, bisect_right

# # 1 2 3 4 4 4 5 6 7 8
# print(bisect_left(nums, 4))
# print(bisect_right(nums, 4))

#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#


def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
    basic_items = f"https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={parentId}"
    avg_set = []
    basic = requests.get(basic_items)
    total_pages = basic.json()["total_pages"]
    for i in range(1, total_pages+1):
        url_items = f"https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={i}"
        response = requests.get(url_items)
        datas = response.json()['data']
        for data in datas:
            try:
                parent = data['parent']
                if parent['id'] == parentId:
                    if data['operatingParams']['rotorSpeed']:
                        avg_set.append(data['operatingParams']['rotorSpeed'])
            except:
                continue
    return sum(avg_set) // len(avg_set)


print(avgRotorSpeed('RUNNING', 7))

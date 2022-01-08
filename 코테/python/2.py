import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque

def joinlist(stones):
    return "".join(map(str, stones))

def getNums(stones):
    return int(joinlist(stones))

def isOne(stones, k):
    strs = "".join(map(str, stones)).replace("0", "")
    if len(strs) == 1 and int(strs) == k:
        return True
    else:
        return False

def solution(stones, k):
    if max(stones) + min(stones) < k:
        return "-1" 
    answer = ''
    strs = joinlist(stones)
    S = getNums(stones)
    results = []


    def bfs(stones, result):
        visited = { "" }
        Q = deque([[stones[::], ""]])
        num = 9999999999
        results = []
        while Q:
            _stones, result = Q.popleft()
            stone_num = getNums(_stones)
            stone_plus = []
            if num < len(result):
                continue
            if isOne(_stones, k):
                num = min(num, len(result))
                results.append(result)
            for stone in _stones:
                stone_plus.append(stone - 1)
            for i in range(len(_stones)):
                _stone_plus = stone_plus[::]
                _stone_plus[i] = _stone_plus[i] + 2
                strs = joinlist(_stone_plus) + str(i)
                if joinlist(_stone_plus).count("-") >= 1:
                    continue
                visited.add(strs)
                Q.append([_stone_plus, result + str(i)])
        return results
    results = bfs(stones, "")
    results.sort(reverse=True)    
    return results[0]


# print(solution([1, 3, 2], 3))
print(solution([4, 2, 2, 1, 4], 1))
# print(solution([5, 7, 2, 4, 9], 20))

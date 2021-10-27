import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque

def two(n):
    return n ^ ((n & -n) << 1)

def one(n):
    return n ^ 1

visited = [False] * 100

def solution(n):
    Q = deque([n])
    visited[n] = 1
    func = [one, two]
    while Q:
        u = Q.popleft()
        if u == 0:
            return visited[0] - 1
        for calc in func:
            v = calc(u)
            if not visited[v]:
                visited[v] = visited[u] + 1
                Q.append(v)

print(solution(13))

import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque

def two(n):
    return n ^ (n & -n >> 1)

def one(n):
    return n ^ 1

dp = [False] * 100

def go(n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = 0
    dp[n] = max(go(one(n)) + 1, go(two(n)) + 1)
    return dp[n] 

def solution(n):
    go(n)
    return dp[n]


print(solution(11))
print(dp)

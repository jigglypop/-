import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque


def solution(l, r):
    return [i for i in range(l, r+1) if i % 2 == 1]


print(solution(1, 8))

import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque


def oddNumbers(l, r):
    # Write your code here
    return [i for i in range(l, r+1) if i % 2 == 1]


print(oddNumbers(1, 8))

import math
import os
import random
import re
import sys
from pprint import pprint
from collections import deque


def oddNumbers(l, r):
    # Write your code here
    Q = deque()
    Q.append(1)
    print(Q)
    return [i for i in range(l, r+1) if i % 2 == 1]


print(oddNumbers(1, 8))

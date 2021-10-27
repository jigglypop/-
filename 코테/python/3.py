import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque
import ipaddress


def is4(address): 
    for add in address.split("."): 
        if len(add) == 0: 
            return False
        if len(add) > 3: 
            return False
        if add.isdigit() == False: 
            return False
        if add[0] == '0' and len(add) != 1: 
            return False
        if int(add) > 255: 
            return False
    return True

def is6(address): 
    _address = address.split(":")
    if len(_address) < 8 and "::" not in address:
        return False
    for add in _address: 
        if add == "": 
            continue
        if len(add) == 0 or len(add) > 4: 
            return False 
        for a in add: 
            if a.lower() not in '0123456789abcdef': 
                return False 
    return True

def solution(addresses):
    result = []
    for add in addresses:
        if is4(add):
            result.append('IPv4')
        elif is6(add):
            result.append("IPv6")
        else:
            result.append("Neither")
    return result

print(solution([
"143.187.220.001",
]))

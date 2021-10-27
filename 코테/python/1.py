import math
import os
import random
import re
import sys
from pprint import pprint
# 임포트 모듈
from collections import deque

def solution(nodes):
    _nodes = nodes.split(" ")
    tree = [[] * 26 for _ in range(26)]
    up = [[] * 26 for _ in range(26)]
    down = [[] * 26 for _ in range(26)]
    node_set = set()
    for _node in _nodes:
        a, b = _node.replace("(", "").replace(")", "").split(",")
        a = ord(a) - 65
        b = ord(b) - 65
        node_set.add(a)
        node_set.add(b)
        if b in tree[a]:
            return 'E2'
        if a in tree[b]:
            return 'E2'
        tree[a].append(b)
        tree[b].append(b)
        up[a].append(b)
        down[b].append(a)
    for t in tree:
        if len(t) > 2:
            return "E1"
    root = []
    for i in range(26):
        if len(up[i]) != 0 and len(down[i]) == 0:
            root.append(i)
    if len(root) > 1:
        return "E4"
    if len(node_set) -1 != len(_nodes):
        return "E3"

    visited = [False] * 26
    visited[root[0]] = True
    def dfs(u):
        result = "(" + chr(u + 65)
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                result += dfs(v)
        return result + ")"
    result = dfs(root[0])
    if result:
        return result
    return "E5"


print(solution("(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)"))

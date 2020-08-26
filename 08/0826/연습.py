
import sys
from itertools import combinations
from string import ascii_lowercase
from collections import defaultdict
sys.stdin = open("DICTIONARY.txt", "r")
#input=lambda: f.readline()


def DFS(cur):
    if visited[cur]:
        return
    visited[cur] = True
    for i in graph[cur]:
        if not visited[i]:
            DFS(i)
    order.append(cur)


for _ in range(int(input())):
    words = [input() for _ in range(int(input()))]
    graph = defaultdict(list)
    for i in range(len(words)-1):
        word_left, word_right = words[i], words[i+1]
        n = min(len(word_left), len(word_right))
        for j in range(n):
            if word_left[j] != word_right[j]:
                if word_left[j] in graph[word_right[j]]:
                    continue
                graph[word_right[j]].append(word_left[j])
                break
    visited = {char: False for char in ascii_lowercase}
    order = []
    for char in ascii_lowercase:
        DFS(char)

    if any(char_left in graph and char_right in graph[char_left]
            for char_left, char_right in combinations(order, 2)):
        print('INVALID HYPOTHESIS')
    else:
        print(''.join(order))

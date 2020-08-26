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
    for next_node in graph[cur]:
        if not visited[cur]:
            DFS(cur)
    order.append(cur)


for _ in range(int(input())):
    words = [input() for _ in range(int(input()))]
    # Make Graph
    # adj_graph = {}
    # for word_left, word_right in zip(words, words[1:]):
    #     for char_left, char_right in zip(word_left, word_right):
    #         if char_left != char_right:
    #             adj_graph.setdefault(char_right, set()).add(char_left)
    #             break
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
    # Print Order
    if any(char_left in graph and char_right in graph[char_left]
            for char_left, char_right in combinations(order, 2)):
        print('INVALID HYPOTHESIS')
    else:
        print(''.join(order))

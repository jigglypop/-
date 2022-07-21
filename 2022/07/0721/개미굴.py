from pprint import pprint
import sys
sys.stdin = open('./text/14275.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

trie = {}
for _ in range(Int()):
    word = input().split()
    parent = trie
    for a in word[1:]:
        if a not in parent:
            parent[a] = {}
        parent = parent[a]

def dfs(parent, level):
    for k, v in sorted(parent.items()):
        print("--" * level + k)
        dfs(v, level + 1)

dfs(trie, 0)
from pprint import pprint
import sys
sys.stdin = open('./text/5052.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    trie = {}
    words = [list(input().rstrip()) + ["*"] for _ in range(Int())]
    words.sort(key=lambda x: len(x))
    
    def go():
        for word in words:
            parent = trie
            for a in word:
                if a not in parent:
                    parent[a] = {}
                parent = parent[a]
                if "*" in parent:
                    return "NO"
        return "YES"

    print(go())

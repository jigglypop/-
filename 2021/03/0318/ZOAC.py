import sys
sys.stdin = open("16719.txt", "r")
words = list(input())
edges = []
for i in range(len(words)):
    word = words[i]
    edges.append((ord(word) - 65, i))
print(edges)

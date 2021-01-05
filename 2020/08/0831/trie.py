from collections import defaultdict
from pprint import pprint


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

    def __repr__(self):
        return f'TrieNode({self.word} :{self.children.items()})'


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 삽입
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
    # 단어 존재 여부 판별

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    # 문자열로 시작 단어 존재 여부 판별

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.childern:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert("apple")
trie.insert("appeal")
trie.insert("appear")

print(trie.search("apple"))
pprint(trie.root)

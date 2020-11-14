class Node:
    def __init__(self):
        self.children = [-1] * 26
        self.pi = -1
        self.valid = False

    def __repr__(self):
        result = None
        next_node = []
        for i in range(26):
            if self.children[i] != -1:
                result = chr(i+ord('a'))
                next_node.append(self.children[i])
        return f"Node({result}:{next_node})"


def init():
    x = Node()
    trie.append(x)
    return len(trie)-1


def add(node, s, index):
    if index == len(s)-1:
        trie[node].valid = True
        return
    c = ord(s[index].lower()) - ord('a')
    if trie[node].children[c] == -1:
        next = init()
        trie[node].children[c] = next
    add(trie[node].children[c], s, index+1)


def search(node, s, index):
    if node == -1:
        return False
    if index == len(s)-1:
        return trie[node].valid
    c = ord(s[index].lower()) - ord('a')
    child = trie[node].children[c]
    return search(child, s, index + 1)


trie = []
root = init()
add(root, 'apple', 0)
add(root, 'appeal', 0)
print(trie)
print(search(root, 'appea', 0))

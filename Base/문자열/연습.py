class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for w in word:
            if w not in cur:
                print(w)
                return False
            cur = cur[w]
        if '*' in cur:
            return True
        else:
            return False


dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hey"))

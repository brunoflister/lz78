class TrieNode():
    def __init__(self, code, char):
        self.code = code
        self.char = char
        self.endof = False
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode(0, '')

    def insert(self, index, word):
        current = self.root
        for char in word:
            if char not in current.children:
                new = TrieNode(index,char)
                current.children[char] = new
            current = current.children[char]                      
        current.endof = True

    def search(self, word):
        current = self.root
        if word == '':
            return 0
        for char in word:
            if char not in current.children:
                return -1
            current = current.children[char]
        if not current.endof:
            return -1
        return current.code
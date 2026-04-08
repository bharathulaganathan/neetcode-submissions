class Trie:
    def __init__(self):
        self.sub = dict()
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.sub:
                cur.sub[w] = Trie()
            cur = cur.sub[w]
        cur.end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.sub:
                return False
            cur = cur.sub[w]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.sub:
                return False
            cur = cur.sub[w]
        return True
        
        
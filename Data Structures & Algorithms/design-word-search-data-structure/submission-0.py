class Trie:
    def __init__(self):
        self.sub = dict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.sub:
                cur.sub[w] = Trie()
            cur = cur.sub[w]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        self.found = False
        def find_dot(rem, cur):
            if len(rem) == 0:
                self.found = cur.end
                return
            if rem[0] == "." and cur.sub:
                for v in cur.sub.values():        
                    find_dot(rem[1:], v)
            else:
                if rem[0] in cur.sub:
                    find_dot(rem[1:], cur.sub[rem[0]])
        find_dot(word, cur)
        return self.found
                


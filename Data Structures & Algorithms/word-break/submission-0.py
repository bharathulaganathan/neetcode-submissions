class Node:
    def __init__(self):
        self.child = dict()
        self.end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node()
        for word in wordDict:
            cur = root
            for c in word:
                if c not in cur.child:
                    cur.child[c] = Node()
                cur = cur.child[c]
            cur.end = True
        n = len(s)
        end = set()
        for i in range(n-1,-1,-1):
            idx = i
            char = s[i]
            node = root
            for j in range(i,n):
                if s[j] in node.child:
                    node = node.child[s[j]]
                    if node.end and (j+1 in end or j == n-1):
                        end.add(i)
                else:
                    break
        return 0 in end


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = dict()
        dep = dict()
        for w in words:
            for c in w:
                graph[c] = set()
                dep[c] = set()
        for i in range(n-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    dep[words[i+1][j]].add(words[i][j])
                    break
            else:
                if len(words[i+1]) > len(words[i]):
                    return str()
        q = deque()
        for k, v in dep.items():
            l = len(v)
            dep[k] = l
            if l == 0:
                q.append(k)
        res = str()
        done = set()
        while q:
            c = q.popleft()
            done.add(c)
            res += c
            for a in graph[c]:
                if a not in done:
                    dep[a] -= 1
                    if dep[a] == 0:
                        q.append(a)
        if len(res) != len(graph):
            return str()
        return res

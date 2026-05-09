class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        head = set()
        tail = set()
        graph = defaultdict(set)
        all_c = set()
        for w in words:
            for c in w:
                all_c.add(c)
        for i in range(n-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    if words[i][j] not in tail:
                        head.add(words[i][j])
                    tail.add(words[i+1][j])
                    if words[i+1][j] in head:
                        head.remove(words[i+1][j])
                    break
            else:
                if len(words[i+1]) > len(words[i]):
                    return str()
        for k, v in graph.items():
            v = list(v)
            graph[k] = v
        if len(head) == 0:
            return str()
        for c in head:
            done = set()
            q = [c]
            while q:
                cur = q.pop()
                if cur in done:
                    return str()
                done.add(cur)
                q.extend(graph[cur])
        cur = list(head)[0]
        res = cur
        all_c.remove(cur)
        while graph[cur]:
            cur = graph[cur][0]
            all_c.remove(cur)
            res += cur
        all_c = "".join(list(all_c))
        return res + all_c
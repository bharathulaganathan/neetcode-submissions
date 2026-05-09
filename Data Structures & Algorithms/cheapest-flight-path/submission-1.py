class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airports = [[] for _ in range(n)]
        price = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, c in flights:
            airports[s].append(d)
            price[s][d] = c
        cost = [math.inf] * n
        cost[src] = 0
        q = set([src])
        visited = set()
        for _ in range(k+1):
            nq = set()
            q = list(q)
            while q:
                cur = q.pop()
                visited.add(cur)
                for d in airports[cur]:
                    cost[d] = min(cost[d], cost[cur] + price[cur][d])
                    nq.add(d)
            q = nq
        return -1 if cost[dst] == math.inf else cost[dst]
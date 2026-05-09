class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airports = [[] for _ in range(n)]
        price = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, c in flights:
            airports[s].append(d)
            price[s][d] = c
        cost = [math.inf] * n
        cost[src] = 0
        q = [src]
        for _ in range(k+1):
            nq = set()
            rev_cost = dict()
            while q:
                cur = q.pop()
                for d in airports[cur]:
                    new_cost = cost[cur] + price[cur][d]
                    if new_cost < cost[d]:
                        if d in rev_cost:
                            rev_cost[d] = min(new_cost, rev_cost[d])
                        else:
                            rev_cost[d] = new_cost
                        nq.add(d)
            for d in rev_cost.keys():
                cost[d] = rev_cost[d]
            q = list(nq)
        return -1 if cost[dst] == math.inf else cost[dst]
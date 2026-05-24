class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [math.inf] * (amount+1)
        res[amount] = 0
        q = deque()
        q.append(amount)
        while q:
            cur = q.popleft()
            val = res[cur]
            for c in coins:
                if cur - c < 0:
                    continue
                if res[cur-c] > val + 1:
                    res[cur-c] = val + 1
                    q.append(cur-c)
        return -1 if res[0] == math.inf else res[0]
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while sum(counter.values()) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

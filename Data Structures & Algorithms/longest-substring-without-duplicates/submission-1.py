class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        c = set(s[0])
        res = 1
        while r < len(s):
            if s[r] in c:
                res = max(res, r-l)
                while s[l] != s[r]:
                    c.remove(s[l])
                    l += 1
                l += 1
                r += 1
            else:
                c.add(s[r])
                r += 1
        return max(res, r-l)
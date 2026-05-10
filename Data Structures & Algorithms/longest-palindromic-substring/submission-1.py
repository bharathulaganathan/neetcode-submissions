class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]
        l = r = 0
        while r < n:
            if s[l] == s[r]:
                for i in range(0,min(l,n-r-1)+1):
                    if s[l-i] != s[r+i]:
                        if len(s[l-i+1:r+i]) > len(res):
                            res = s[l-i+1:r+i]
                        break
                else:
                    if len(s[l-i:r+i+1]) > len(res):
                        res = s[l-i:r+i+1]

            if l == r:
                r += 1
            else:
                l += 1
        return res
        
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) <= n:
            l = len(res)
            for i in range(0,min(l,n-l+1)):
                res.append(res[i]+1)
        return res
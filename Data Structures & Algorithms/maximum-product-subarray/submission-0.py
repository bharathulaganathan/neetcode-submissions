class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low = nums[-1]
        high = nums[-1]
        for n in nums:
            nlow = min(n,high*n,low*n)
            nhigh = max(n,high*n,low*n)
            low = nlow
            high = nhigh
        return high
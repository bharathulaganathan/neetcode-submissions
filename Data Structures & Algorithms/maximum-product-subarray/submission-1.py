class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low = high = res = nums[0]
        nums.pop(0)
        for n in nums:
            nlow = min(n,high*n,low*n)
            nhigh = max(n,high*n,low*n)
            low = nlow
            high = nhigh
            res = max(res,high)
        return res
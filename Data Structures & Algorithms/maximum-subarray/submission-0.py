class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = max(res+nums[i],nums[i])
        return res

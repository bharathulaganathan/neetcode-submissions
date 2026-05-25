class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for i in range(1,len(nums)):
            cur = max(cur+nums[i],nums[i])
            res = max(res,cur)
        return res

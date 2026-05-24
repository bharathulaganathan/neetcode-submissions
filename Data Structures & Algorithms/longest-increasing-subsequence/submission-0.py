class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = [1] * n
        for i in range(n):
            cur = res[i] + 1
            num = nums[i]
            for j in range(i+1,n):
                if nums[j] > num:
                    res[j] = max(res[j], cur)
        return max(res)
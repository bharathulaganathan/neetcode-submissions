class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = 0
        for i in range(n):
            if i > r:
                return False
            if nums[i] + i > r:
                r = nums[i] + i
            if r >= n - 1:
                return True
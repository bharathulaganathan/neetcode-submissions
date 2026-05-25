class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(nums[-1]):
            if nums[i] != i:
                return i
        return nums[-1] + 1
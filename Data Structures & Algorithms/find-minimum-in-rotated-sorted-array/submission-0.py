class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n
        res = nums[0]
        mid = (r - l) // 2
        while mid > l:
            m = nums[mid]
            if m > res:
                l = mid
                mid += (r - l) // 2
            elif m < res:
                res = m
                r = mid
                mid -= (r - l) // 2
            else:
                break
        return res
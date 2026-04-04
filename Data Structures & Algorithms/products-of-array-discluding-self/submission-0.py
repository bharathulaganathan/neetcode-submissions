class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left = [1]
        right = [1]
        for i in range(nums_len):
            left.append(left[-1]*nums[i])
            right.insert(0,right[0]*nums[-(i+1)])
        res = []
        for i in range(nums_len):
            res.append(left[i]*right[i+1])
        return res
        
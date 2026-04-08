class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        self.nums = nums
        def find_subset(i, arr):
            if i >= len(self.nums):
                res.append(arr)
                return
            new_arr = arr.copy()
            new_arr.append(self.nums[i])
            i += 1
            find_subset(i, arr)
            find_subset(i, new_arr)
            return
        find_subset(0, list())
        return res
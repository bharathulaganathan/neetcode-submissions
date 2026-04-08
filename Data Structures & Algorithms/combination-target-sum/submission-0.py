class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        def find_comb(i, total, num):
            if total == target:
                res.append(num)
                return
            if total > target:
                return
            for n in range(i, len(nums)):
                new_num = num.copy()
                new_num.append(nums[n])
                find_comb(n, total + nums[n], new_num)
        find_comb(0, 0, list())
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            j = 0
            k = n-1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
                if nums[j] + nums[k] == -nums[i]:
                    ans = [nums[i], nums[j], nums[k]]
                    ans.sort()
                    ans = tuple(ans)
                    res.add(ans)
                    j += 1
                    k -= 1
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
        res = list(res)
        res = list(map(list,res))
        return res

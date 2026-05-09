class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        mem = dict()
        def robs(x):
            if x == n:
                return 0
            if x == n-1:
                return nums[n-1]
            if x == n-2:
                return nums[n-2]
            if x+2 not in mem:
                mem[x+2] = robs(x+2)
            skip = mem[x+2]
            if x+3 not in mem:
                mem[x+3] = robs(x+3)
            jump = mem[x+3]
            return nums[x] + max(skip, jump)
        return max(robs(0),robs(0))
        
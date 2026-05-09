class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        mem = dict()
        def robs(x,s):
            if x == n:
                return 0
            if x == n-1:
                if s == 0:
                    return 0
                return nums[n-1]
            if x == n-2:
                return nums[n-2]
            if x+2 not in mem:
                mem[x+2] = dict()
            if s not in mem[x+2]:
                mem[x+2][s] = robs(x+2,s)
            skip = mem[x+2][s]
            if x+3 not in mem:
                mem[x+3] = dict()
            if s not in mem[x+3]:
                mem[x+3][s] = robs(x+3,s)
            jump = mem[x+3][s]
            return nums[x] + max(skip, jump)
        return max(robs(0,0),robs(1,1))
        
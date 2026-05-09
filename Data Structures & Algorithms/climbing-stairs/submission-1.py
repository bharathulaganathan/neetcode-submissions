class Solution:
    def climbStairs(self, n: int) -> int:
        mem = dict()
        def steps(x):
            if x == 1:
                return 1
            if x == 2:
                return 2
            if x-1 not in mem:
                mem[x-1] = steps(x-1)
            last = mem[x-1]
            if x-2 not in mem:
                mem[x-2] = steps(x-2)
            pen = mem[x-2]
            return last + pen
        return steps(n)

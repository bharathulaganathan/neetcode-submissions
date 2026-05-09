class Solution:
    def climbStairs(self, n: int) -> int:
        mem = dict()
        def steps(x):
            if x == 1:
                return 1
            if x == 2:
                return 2
            last = mem[x-1] if x-1 in mem else steps(x-1)
            pen = mem[x-2] if x-2 in mem else steps(x-2)
            return last + pen
        return steps(n)

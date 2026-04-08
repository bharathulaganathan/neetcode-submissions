class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def find_subset(done, rem):
            if done:
                done.sort()
            res.add(tuple(done))
            for r in range(len(rem)):
                new = done.copy()
                new.append(rem[r])
                find_subset(new, rem[:r]+rem[r+1:])
            return
        find_subset(list(),nums)
        res = list(map(list,res))
        return res
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed_list = {}
        for i in range(len(strs)):
            hashed_str = {}
            for j in range(len(strs[i])):
                hashed_str[strs[i][j]] = hashed_str.get(strs[i][j],0) + 1
            hashed_str = list(hashed_str.items())
            hashed_str.sort()
            hashed_str = tuple(hashed_str)
            hashed_list.setdefault(hashed_str, []).append(strs[i])
        res = []
        for key in hashed_list.keys():
            res.append(hashed_list[key])
        return res
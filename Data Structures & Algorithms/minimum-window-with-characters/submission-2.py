class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = len(s)
        target = dict()
        for i in range(len(t)):
            target[t[i]] = target.get(t[i], 0) + 1
        target_copy = target.copy()
        res = ""
        found = dict()
        for r in range(len(s)):
            if s[r] in target:
                target[s[r]] -= 1
                found[s[r]] = found.get(s[r], 0) + 1
                if target[s[r]] == 0:
                    target.pop(s[r])
                l = min(l, r)
            elif s[r] in found:
                found[s[r]] += 1
            if len(target) == 0:
                res = s[l:r+1]
                res_len = r - l + 1
                break
        if not res:
            return res
        target = target_copy
        while l < len(s):
            if s[l] in target:
                if found[s[l]] > target[s[l]]:
                    found[s[l]] -= 1
                elif found[s[l]] == target[s[l]]:
                    res_len = r - l + 1
                    res = s[l:r+1]
                    break
            l += 1
        for r in range(r+1,len(s)):
            if s[r] in target:
                if s[l] == s[r]:
                    l += 1
                    while True:
                        if s[l] in target:
                            if found[s[l]] > target[s[l]]:
                                found[s[l]] -= 1
                            else:
                                break
                        l += 1
                    if r - l + 1 < res_len:
                        res_len = r - l + 1
                        res = s[l:r+1]
                else:
                    found[s[r]] += 1
        return res

class Solution:
    def isValid(self, s: str) -> bool:
        b = list()
        check = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in ["(", "{", "["]:
                b.append(c)
            else:
                if (b[-1] if b else None) == check[c]:
                    b.pop()
                else:
                    return False
        return not b
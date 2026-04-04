class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "." + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        s_len = len(s)
        while i < s_len:
            val = ""
            while s[i] != ".":
                val += s[i]
                i += 1
            i += 1
            val = int(val)
            decoded.append(s[i:i+val])
            i += val
        return decoded
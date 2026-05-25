class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:][::-1]
        b = b + "0"*(32-len(b))
        return int(b,2)
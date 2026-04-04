class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = ""
        reverse = ""
        for c in s:
            if c.isalnum():
                c = c.lower()
                original = original + c
                reverse = c + reverse
        return original == reverse

        
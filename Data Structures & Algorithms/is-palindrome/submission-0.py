class Solution:
    def isPalindrome(self, s: str) -> bool:

        sstrs = ''

        for c in s:
            if c.isalnum(): sstrs += c.lower()

        return sstrs == sstrs[::-1]

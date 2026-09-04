class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        l, r = 0, 0

        while l < len(t) and r < len(s):
            if s[r] == t[l]: l += 1
            r += 1

        return len(t) - l
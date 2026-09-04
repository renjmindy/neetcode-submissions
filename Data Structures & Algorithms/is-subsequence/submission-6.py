class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0: return True
        if len(t) == 0: return False

        l, r = 0, 0

        while r < len(t):
            if s[l] == t[r] and l < len(s) - 1 and r < len(t) - 1: l += 1
            r += 1

        return l == len(s) - 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0: return True
        if len(t) == 0: return False
        
        l = 0

        for r in range(len(t)):
            if t[r] == s[l] and r < len(t) - 1 and l < len(s) - 1: l += 1

        return l == len(s) - 1
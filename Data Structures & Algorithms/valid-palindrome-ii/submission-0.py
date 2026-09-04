class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]: return True

        for r in range(len(s)):
            t = s[:r] + s[r + 1:]
            if t == t[::-1]: return True 
            

        return False
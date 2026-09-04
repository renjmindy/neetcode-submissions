class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        r1, r2 = 0, 0
        ans = ''

        while r1 < len(word1) or r2 < len(word2):
            if r1 < len(word1): ans += word1[r1]; r1 += 1
            if r2 < len(word2): ans += word2[r2]; r2 += 1

        return ans
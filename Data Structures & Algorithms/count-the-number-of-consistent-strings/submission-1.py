class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        ans = 0

        p = set(allowed)

        for word in words:
            if all(c in p for c in word): ans += 1

        return ans

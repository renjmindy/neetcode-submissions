class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        mp = dict(Counter(allowed))
        ans = 0
        found = False

        for word in words:
            np = dict(Counter(word))
            found = False
            for k, v in np.items():
                if k not in mp: found = True; break
            if not found: ans += 1

        return ans
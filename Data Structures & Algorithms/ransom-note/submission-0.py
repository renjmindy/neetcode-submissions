class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mp = Counter(magazine)
        np = Counter(ransomNote)

        for k, v in np.items():
            if k not in mp: return False
            else:
                if v > mp[k]: return False

        return True
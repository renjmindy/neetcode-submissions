class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        mp, np = defaultdict(int), defaultdict(int)

        for l in range(len(s1)):
            mp[s1[l]] += 1
            np[s2[l]] += 1

        if mp == np: return True

        l = 0

        for r in range(len(s1), len(s2)):
            np[s2[l]] -= 1
            np[s2[r]] += 1

            if np[s2[l]] == 0: np.pop(s2[l])

            if mp == np: return True

            l += 1

        return False

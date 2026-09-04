class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mp = Counter(t)

        l, cnts = 0, 0

        ans = ''

        for r in range(len(s)):
            if mp[s[r]] > 0: cnts += 1
            mp[s[r]] -= 1

            if cnts == len(t):
                while l < len(s) and mp[s[l]] < 0:
                    mp[s[l]] += 1
                    l += 1

                if len(ans) == 0 or len(ans) > (r - l + 1):
                    ans = s[l:r + 1]

        return ans

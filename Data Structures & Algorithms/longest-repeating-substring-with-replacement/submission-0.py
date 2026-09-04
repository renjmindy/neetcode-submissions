class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mp = defaultdict(int)
        l, cnts, ans = 0, 0, 0

        for r in range(len(s)):
            mp[s[r]] += 1
            cnts = max(cnts, mp[s[r]])

            while r - l + 1 - cnts > k:
                mp[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
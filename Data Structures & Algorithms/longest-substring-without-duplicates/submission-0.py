class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = defaultdict(int)
        l, ans = 0, 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]])

            mp[s[r]] = r + 1
            ans = max(ans, r - l + 1)

        return ans
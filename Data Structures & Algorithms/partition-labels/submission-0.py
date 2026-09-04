class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mp = defaultdict(int)

        l, r = 0, 0

        ans = list()

        for i, c in enumerate(s):
            mp[c] = i

        for i in range(len(s)):
            r = max(r, mp[s[i]])

            if r == i:
                ans.append(r - l + 1)
                l = i + 1

        return ans
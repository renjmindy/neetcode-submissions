class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l, ans = 0, 0
        mp = defaultdict(int)

        for r in range(len(fruits)):
            mp[fruits[r]] += 1
            while len(mp) > 2:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] == 0: mp.pop(fruits[l])
                l += 1
            ans = max(ans, r - l + 1)

        return ans
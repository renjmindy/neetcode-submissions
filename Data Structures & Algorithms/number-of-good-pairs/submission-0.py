class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        mp = defaultdict(list)
        ans = 0

        for i, num in enumerate(nums):
            mp[num].append(i)

        for k, v in mp.items():
            ans += (len(v) * (len(v) - 1)) // 2

        return ans
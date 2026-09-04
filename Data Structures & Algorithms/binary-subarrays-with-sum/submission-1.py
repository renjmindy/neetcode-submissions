class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        mp = defaultdict(int)
        mp[0] = 1

        cnt, ans = 0, 0

        for i, num in enumerate(nums):
            cnt += num
            ans += mp[cnt - goal]
            mp[cnt] += 1

        return ans
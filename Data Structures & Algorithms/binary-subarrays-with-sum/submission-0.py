class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        mp = {0:1}

        cnt, ans = 0, 0

        for i, num in enumerate(nums):
            cnt += num
            ans += mp.get(cnt - goal, 0)
            mp[cnt] = mp.get(cnt, 0) + 1 

        return ans
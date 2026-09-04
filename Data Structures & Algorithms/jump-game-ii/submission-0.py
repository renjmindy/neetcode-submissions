class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return 0

        mp = [0] * len(nums)

        mp[0] = nums[0]

        for r in range(1, len(nums)):
            mp[r] = max(mp[r - 1], r + nums[r])

        cnt, ans = 0, 0

        while cnt < len(nums) - 1:
            ans += 1
            cnt = mp[cnt]

        return ans 


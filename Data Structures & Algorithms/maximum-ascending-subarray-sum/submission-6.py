class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        if len(set(nums)) == 1: return nums[0]

        inc, sum, ans = 1, 0, nums[0]

        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                if inc == 1:
                    sum += nums[r - 1]
                    sum += nums[r]
                else:
                    sum += nums[r]
                inc += 1
            else:
                inc = 1
                ans = max(ans, sum)
                sum = 0

        return max(ans, sum)

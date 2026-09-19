class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0

        nums.sort()

        for num in nums:
            ans ^= num

        return ans
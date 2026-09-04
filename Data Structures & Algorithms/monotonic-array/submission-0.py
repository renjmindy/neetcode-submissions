class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        ans = list()

        for r in range(1, len(nums)):
            ans.append(nums[r] - nums[r - 1])

        return all(x >= 0 for x in ans) or all(x <= 0 for x in ans)





        
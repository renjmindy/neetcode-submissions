class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        mums = list(set(nums))
        mums.sort()
        ans = list()

        for i in range(1, len(nums) + 1):
            if i in mums: continue
            else: ans.append(i)

        return ans
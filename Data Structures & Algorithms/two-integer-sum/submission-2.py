class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = list()
        res = defaultdict()

        for i, num in enumerate(nums):
            if target - num in res:
                ans.append(res[target - num])
                ans.append(i)
            res[num] = i

        return ans
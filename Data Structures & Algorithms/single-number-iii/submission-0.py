class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        mp = dict(Counter(nums))
        ans = list()

        for k, v in mp.items():
            if v == 1: ans.append(k)

        return ans
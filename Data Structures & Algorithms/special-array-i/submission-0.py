class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        p = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        q = [nums[i] for i in range(len(nums)) if i % 2 == 1]

        all_even_p = all(x % 2 == 0 for x in p)
        all_odd_p = all(x % 2 == 1 for x in p)

        all_even_q = all(x % 2 == 0 for x in q)
        all_odd_q = all(x % 2 == 1 for x in q)

        return (all_even_p == True and all_odd_q == True) or (all_odd_p == True and all_even_q == True)
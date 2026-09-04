class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ans = list()
        mp = defaultdict(int)

        for i, num in enumerate(numbers):
            if target - num in mp:
                ans.append(mp[target - num])
                ans.append(i + 1)

            mp[num] = i + 1

        return ans
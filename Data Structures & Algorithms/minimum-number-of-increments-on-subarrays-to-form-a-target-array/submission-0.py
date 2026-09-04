class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        ans = target[0]

        for r in range(1, len(target)):
            if target[r] > target[r - 1]: ans += (target[r] - target[r - 1])

        return ans
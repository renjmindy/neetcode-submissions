class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        if k == 1: return 0

        ans = list()

        for r in range(len(weights) - 1):
            ans.append(weights[r] + weights[r + 1])

        ans.sort()

        return sum(ans[-(k - 1):]) - sum(ans[:k - 1])
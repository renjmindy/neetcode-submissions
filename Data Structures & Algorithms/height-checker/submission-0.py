class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)

        ans = 0

        for i, height in enumerate(heights):
            if height != expected[i]: ans += 1

        return ans
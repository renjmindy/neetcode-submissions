class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = list()

        for r in range(0, len(num) - 2):
            if len(set(num[r:r + 3])) == 1: ans.append(num[r:r + 3])

        return max(ans) if ans else ''
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        ans = list()
        pre = heights[-1]
        ans.append(len(heights) - 1)

        for r in range(len(heights) - 2, -1, -1):
            pre = max(heights[r+1:])
            if heights[r] > pre: ans.append(r)

        return ans[::-1]  
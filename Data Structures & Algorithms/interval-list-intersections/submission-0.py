class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        l, r = 0, 0

        ans = list()

        while l < len(firstList) and r < len(secondList):
            ini = max(firstList[l][0], secondList[r][0])
            end = min(firstList[l][1], secondList[r][1])

            if ini <= end: ans.append([ini, end])

            if firstList[l][1] <= secondList[r][1]: l += 1
            else: r += 1

        return ans
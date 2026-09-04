class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        size = len(grid) * len(grid[0])

        p, q, ans = list(), set(), list()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                p.append(grid[i][j])

        q = set(p)
        mp = Counter(p)

        for k, v in mp.items():
            if v > 1: ans.append(k)

        for i in range(1, size + 1):
            if i not in q: ans.append(i)

        return ans

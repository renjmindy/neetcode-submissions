class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        size = len(grid) * len(grid[0])

        p, ans = list(), list()
        q = [i for i in range(1, size + 1)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                p.append(grid[i][j])

        r = p + q
        mp = Counter(r)
        mp_sort = dict(sorted(mp.items(), key = lambda x:x[1], reverse=True))

        for k, v in mp_sort.items():
            if v > 2: ans.append(k)
            if v == 1: ans.append(k)

        return ans

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        r1, r2, cnt = 0, 0, 0

        while r1 < len(g) and r2 < len(s):
            if s[r2] >= g[r1]: cnt += 1; r1 += 1; r2 += 1
            else: r2 += 1

        return cnt
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        v, h = len(boxGrid), len(boxGrid[0])

        ans = [['.'] * v for _ in range(h)]

        for i in range(v):
            p = h - 1
            for j in range(h - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    ans[j][v - i - 1] = "*"
                    p = j - 1
                elif boxGrid[i][j] == "#":
                    ans[p][v - i - 1] = "#"
                    p -= 1

        return ans


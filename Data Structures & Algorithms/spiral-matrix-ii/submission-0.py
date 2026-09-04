class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        l, r, t, b = 0, n, 0, n

        ans = [[0] * n for _ in range(n)]

        num = 1

        while l < r and t < b:

            for j in range(l, r):
                ans[l][j] = num
                num += 1

            t += 1

            for i in range(t, b):
                ans[i][r - 1] = num
                num += 1

            r -= 1

            if t < b:
                for j in range(r - 1, l - 1, -1):
                    ans[b - 1][j] = num
                    num += 1

            b -= 1

            if l < r:
                for i in range(b - 1, t - 1, -1):
                    ans[i][l] = num
                    num += 1

            l += 1

        return ans
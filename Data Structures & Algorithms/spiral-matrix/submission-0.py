class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = list()

        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)

        while len(ans) < len(matrix) * len(matrix[0]):

            for i in range(l, r):
                ans.append(matrix[t][i])

            t += 1

            for j in range(t, b):
                ans.append(matrix[j][r - 1])

            r -= 1

            if t < b:
                for i in range(r - 1, l - 1, -1):
                    ans.append(matrix[b - 1][i])

            b -= 1

            if l < r:
                for j in range(b - 1, t - 1, -1):
                    ans.append(matrix[j][l])

            l += 1

        return ans

            


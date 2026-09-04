class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        ans = 0

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j: ans += mat[i][j]

        #print(ans)

        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat)):
                if i + j == len(mat) - 1: ans += mat[i][j]

        #print(ans)

        if len(mat) % 2: ans -= mat[len(mat) // 2][len(mat) // 2]

        return ans
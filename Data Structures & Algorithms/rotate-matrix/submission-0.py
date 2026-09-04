class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        ans = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        
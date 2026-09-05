class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroR, zeroC = list(), list()

        for i in range(len(matrix)):
            if 0 in matrix[i]: zeroR.append(i)
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: zeroC.append(j)

        for i in zeroR:
            matrix[i] = [0] * len(matrix[i])

        for i in range(len(matrix)):
            for j in zeroC:
                matrix[i][j] = 0

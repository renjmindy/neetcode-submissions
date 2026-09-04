class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            pivot = l + (r - l) // 2
            if matrix[pivot // len(matrix[0])][pivot % len(matrix[0])] < target: l = pivot + 1
            elif matrix[pivot // len(matrix[0])][pivot % len(matrix[0])] > target: r = pivot - 1
            else: return True

        return False
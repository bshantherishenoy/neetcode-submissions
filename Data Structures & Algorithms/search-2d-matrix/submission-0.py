class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        
        col = len(matrix[0])
        row = len(matrix)
        right = (col * row) -1
        while left <= right:
            mid = (left+right)//2
            i = mid // col
            j = mid % col
            value = matrix[i][j]

            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
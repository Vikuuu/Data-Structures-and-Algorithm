from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = (row*col)-1

        while low <= high:
            mid = (low + high) // 2
            search_row = int(mid/col)
            search_col = int(mid%col)
            if matrix[search_row] [search_col] < target:
                low = mid + 1
            elif matrix[search_row][search_col] > target:
                high = mid -1
            else:
                return True
        
        return False
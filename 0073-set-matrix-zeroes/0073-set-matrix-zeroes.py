class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        rows = len(matrix)
        cols = len(matrix[0])
        # First pass — mark rows and columns   
        for row in range(rows):
            for col in range(cols):
                if (matrix[row][col] == 0):
                    matrix[row][0] = 0
                    if col != 0:
                        matrix[0][col] = 0
                    else:
                        col0 = 0
                    
        # Second pass — set zeroes based on markers (from 1,1)     
        for row in range(1,rows):
            for col in range(1,cols):
                if (matrix[row][0] == 0 and matrix[0][col] == 0):
                    matrix[row][col] = 0
        
        # Handle first row separately if needed
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        # Handle first column separately if needed
        if col0 == 0:
            for row in range(rows):
                matrix[row][0] = 0
            
        
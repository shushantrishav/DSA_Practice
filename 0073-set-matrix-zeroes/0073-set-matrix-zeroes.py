class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        n = len(matrix)
        m = len(matrix[0])
        # First pass — mark rows and columns   
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        # Second pass — set zeroes based on markers (from 1,1)     
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Handle first row separately if needed
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Handle first column separately if needed
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
            
        
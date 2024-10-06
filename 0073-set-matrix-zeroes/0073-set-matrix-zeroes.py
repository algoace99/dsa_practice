class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        # Using extra space - O(m*n) - Worst case if all are zero
        index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    index.append([i,j])
        for ele in index:
            matrix[ele[0]] = [0]*len(matrix[ele[0]])
            for i in range(len(matrix)):
                matrix[i][ele[1]] = 0
        return matrix
        '''
        '''
        # With extra space O(m+n) in worst case
        row = [1]*len(matrix)
        col = [1]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row[i] = 0
                    col[j] = 0
        for i in range(len(row)):
            if row[i] == 0:
                matrix[i] = [0]*len(col)
        for i in range(len(col)):
            if col[i] == 0:
                for c in range(len(row)):
                    matrix[c][i] = 0
        '''
        # Without using extra space
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark zeroes in the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Zero out cells based on marks in the first row and first column
        for i in range(1, rows):
            if matrix[i][0] == 0:
                matrix[i] = [0] * cols

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zero:
            matrix[0] = [0] * cols

        # Zero out the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
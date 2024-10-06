class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
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
        
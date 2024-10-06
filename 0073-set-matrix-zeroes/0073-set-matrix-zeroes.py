class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
class Solution:
    def validateArrayContainsDuplicates(self, l: List[str]) -> bool:
        # return True if contains duplicates
        s=set()
        for i in l:
            if i != "." and i in s:
                return True
            s.add(i)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if self.validateArrayContainsDuplicates(row):
                return False

        # Check columns
        for i in range(len(board)):
            column = []
            for j in range(len(board[0])):
                column.append(board[j][i])
            if self.validateArrayContainsDuplicates(column):
                return False

        # Check 3x3 subgrids
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                subgrid = []
                for k in range(3):
                    for l in range(3):
                        subgrid.append(board[i+k][j+l])
                if self.validateArrayContainsDuplicates(subgrid):
                    return False

        return True
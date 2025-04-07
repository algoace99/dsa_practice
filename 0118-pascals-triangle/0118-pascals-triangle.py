class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1],[1,1]]
        if numRows == 2:
            return ans
        for i in range(numRows-2):
            pre = ans[-1]
            temp = []
            for i in range(1,len(pre)):
                temp.append(pre[i-1]+pre[i])
            ans.append([1]+temp+[1])
        return ans
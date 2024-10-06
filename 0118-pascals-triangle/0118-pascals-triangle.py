class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans
        for i in range(numRows - 2):
            pre_ele = ans[-1]
            temp = [1]
            i = 0
            j = 1
            while j < len(pre_ele):
                temp.append(pre_ele[i]+pre_ele[j])
                i+=1
                j+=1
            temp.append(1)
            ans.append(temp)
        return ans
        
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        temp_ans = [1,1]
        for i in range(rowIndex - 1):
            pre_ele = temp_ans
            temp = [1]
            i = 0
            j = 1
            while j < len(pre_ele):
                temp.append(pre_ele[i]+pre_ele[j])
                i+=1
                j+=1
            temp.append(1)
            temp_ans = temp
        return temp_ans
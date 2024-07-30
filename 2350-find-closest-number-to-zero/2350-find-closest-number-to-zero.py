class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        #check if the current element is closest to 0 and update the variable
        #if already same close element present -1 and 1 then update large number
        close = float('inf')
        for i in nums:
            if abs(i)<=abs(close):
                if abs(close)==abs(i):
                    close=max(close,i)
                else:
                    close=i
        return close
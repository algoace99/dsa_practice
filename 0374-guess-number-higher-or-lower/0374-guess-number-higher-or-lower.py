# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            m = (start + end)//2
            ret = guess(m)
            if ret==0:
                return m
            elif ret==1:
                start=m+1
            else:
                end=m-1
        return -1
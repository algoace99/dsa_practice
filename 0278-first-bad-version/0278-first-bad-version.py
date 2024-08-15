# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=0,n
        while l<=r:
            m=l+(r-l)//2
            if isBadVersion(m) and isBadVersion(m-1) is False:
                return m
            elif isBadVersion(m):
                r=m-1
            else:
                l=m+1
        return -1
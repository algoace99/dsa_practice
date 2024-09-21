class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        #return n & (n-1) == 0
        return True if bin(n)[2:].count('1')==1 else False
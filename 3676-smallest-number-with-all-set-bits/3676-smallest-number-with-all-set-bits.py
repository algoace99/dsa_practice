class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            if all(i == "1" for i in list(bin(n)[2:])):
                return n
            n += 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (True if math.floor(math.sqrt(num))**2==num else False)
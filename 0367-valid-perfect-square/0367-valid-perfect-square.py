class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s_r=math.floor(math.sqrt(num))
        if s_r*s_r==num:
            return True
        else:
            return False
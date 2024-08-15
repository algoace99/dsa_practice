class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (True if math.floor(math.sqrt(num))**2==num else False)

        '''
        #two pointer approach without inbuilt methods
        if num<2: return True
        l,r=0,num//2
        while l<=r:
            m=l+(r-l)//2
            sq=m*m
            if sq==num:
                return True
            elif sq<num:
                l=m+1
            else:
                r=m-1
        return False
        '''
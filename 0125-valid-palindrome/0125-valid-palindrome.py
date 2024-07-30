class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        alpha_s = re.sub('[^a-z0-9]', '', lower_s)
        #return True if alpha_s == alpha_s[::-1] else False
        start=0
        end=len(alpha_s)-1
        while(start<end):
            if(alpha_s[start]!=alpha_s[end]):
                return False
            start+=1
            end-=1
        return True
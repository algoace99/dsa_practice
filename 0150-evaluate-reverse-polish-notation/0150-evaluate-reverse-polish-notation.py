class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]
        oprs=['+','-','*','/']
        for i in tokens:
            if i not in oprs:
                ans.append(i)
            elif(i=='+'):
                ans[-2]=int(ans[-2])+int(ans[-1])
                ans.pop()
            elif(i=='-'):
                ans[-2]=int(ans[-2])-int(ans[-1])
                ans.pop()
            elif(i=='*'):
                ans[-2]=int(ans[-2])*int(ans[-1])
                ans.pop()
            elif(i=='/'):
                ans[-2]=math.trunc(int(ans[-2])/int(ans[-1]))
                ans.pop()
        return int(ans[0])
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                stack_i,stack_temp=stack.pop()
                ans[stack_i]=i-stack_i
            stack.append((i,temp))
        return ans
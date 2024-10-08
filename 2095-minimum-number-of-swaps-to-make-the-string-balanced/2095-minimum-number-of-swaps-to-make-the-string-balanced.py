class Solution:
    def minSwaps(self, s: str) -> int:
        '''
        arr = []
        unbalanced = 0
        for i in s:
            if i=="[":
                arr.append(i)
            elif len(arr)!=0:
                arr.pop()
            else:
                unbalanced+=1
        return math.ceil(unbalanced/2)
        '''
        '''
        arr = 0
        unbalanced = 0
        for i in s:
            if i=="[":
                arr+=1
            elif arr > 0:
                arr-=1
            else:
                unbalanced+=1
        return math.ceil(unbalanced/2)
        '''
        unbalanced = 0
        for i in s:
            if i=="[":
                unbalanced+=1
            elif unbalanced > 0:
                unbalanced-=1
            else:
                unbalanced+=1
        return math.ceil(unbalanced/2)
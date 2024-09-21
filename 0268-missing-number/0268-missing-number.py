class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        # Time - O(n)
        # Space - O(n)
        s = set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i
        '''
        ans = 0
        for i in range(1,len(nums)+1):
            ans = ans ^ i
        for n in nums:
            ans = ans ^ n
        return ans

        # Time - O(n)
        # Space - O(1)
        #return (len(nums)*(len(nums)+1)//2)-sum(nums)
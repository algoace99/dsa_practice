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
        # Time - O(n)
        # Space - O(1)
        return (len(nums)*(len(nums)+1)//2)-sum(nums)
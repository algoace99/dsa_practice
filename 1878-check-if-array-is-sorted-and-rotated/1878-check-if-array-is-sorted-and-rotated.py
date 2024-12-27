class Solution:
    def check(self, nums: List[int]) -> bool:
        '''
        # Time = O(n)
        # Space = O(n)
        pivot_element = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot_element = i
                break
        after_rotate = []
        if pivot_element == 0:
            after_rotate = nums
        else:
            after_rotate = nums[i:]+nums[:i]
        if after_rotate == sorted(nums):
            return True
        else:
            return False
        '''
        # Time = O(n)
        # Space = O(1)
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
            if count > 1:
                return False
        return True
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        # Time = O(k*n)
        # Space = O(1)
        for _ in range(k):
            last_ele = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = last_ele
        '''
        # Time = O(n)
        # Space = O(n)
        k = k % len(nums)
        if k != 0:
            nums[:] = nums[len(nums)-k:]+nums[:-k]
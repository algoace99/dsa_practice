class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                index = i-1
                break
        if index == -1:
            nums.reverse()
        else:
            num = -1
            for i in range(len(nums)-1,index,-1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            nums[index+1:] = sorted(nums[index+1:])
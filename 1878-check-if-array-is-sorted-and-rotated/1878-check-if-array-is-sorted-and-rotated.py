class Solution:
    def check(self, nums: List[int]) -> bool:
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
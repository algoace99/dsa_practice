class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dip = -1
        i = len(nums)-1

        # find dip element
        while i > 0:
            if nums[i] > nums[i-1]:
                dip = i-1
                break
            i -= 1

        # if nums are in increasing order
        if dip == -1:
            nums[:] = nums[::-1]
        else:
            # find element which is just greater then dip in right side
            i = len(nums)-1
            swap_ind = -1
            while i >= dip:
                if nums[i] > nums[dip]:
                    swap_ind = i
                    break
                i-=1
            # swap elements
            nums[dip], nums[swap_ind] = nums[swap_ind], nums[dip]

            # revrse remaining elements after dip
            nums[dip+1:] = nums[dip+1:][::-1]
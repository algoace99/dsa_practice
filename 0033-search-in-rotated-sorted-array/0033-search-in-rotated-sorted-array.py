class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target: return 0
            else: return -1
        if len(nums)==2:
            if nums[0]==target: return 0
            elif nums[1]==target: return 1
            else: return -1

        start=1
        end=len(nums)-1
        mini_index=float('inf')

        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]<nums[mid-1]:
                mini_index=mid
                break
            elif nums[mid]>nums[-1]:
                start=mid+1
            else:
                end=mid-1
        if mini_index==float('inf'):
            mini_index=0

        if target<=nums[-1]:
            start=mini_index
            end=len(nums)-1
        else:
            start=0
            end=mini_index
        while(start<=end):
            mid=start+(end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return -1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start=0
        for i in nums:
            if i!=val:
                nums[start]=i
                start+=1
        return start
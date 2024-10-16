class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if any([True if i > 2 else False for i in Counter(nums).values()]):
            return False
        else:
            return True
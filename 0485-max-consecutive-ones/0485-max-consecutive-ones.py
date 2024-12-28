class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_c = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            max_c = max(max_c, count)
        return max_c
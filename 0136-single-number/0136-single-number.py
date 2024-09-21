class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        # Time - O(n)
        # Space - O(n)
        c = Counter(nums)
        for i in c.items():
            if i[1]==1:
                return i[0]
        '''
        # Time - O(n)
        # space - O(1)
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans
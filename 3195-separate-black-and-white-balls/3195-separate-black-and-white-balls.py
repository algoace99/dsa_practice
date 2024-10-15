class Solution:
    def minimumSteps(self, s: str) -> int:
        '''
        left = 0
        count = 0
        for r in range(len(s)):
            if s[r] == "0":
                count += (r-left)
                left += 1
        return count
        '''
        swaps = 0
        zeros = 0
        for i in reversed(range(len(s))):
            if s[i] == '1':
                swaps += zeros
            else:
                zeros += 1
        return swaps
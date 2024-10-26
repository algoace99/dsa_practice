class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        
        for r in range(len(nums)):
            if dq and dq[0] < r - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if r >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans
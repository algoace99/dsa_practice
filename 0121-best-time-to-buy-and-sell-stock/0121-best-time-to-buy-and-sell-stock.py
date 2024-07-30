class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        profit=0
        for i in prices:
            mini=min(mini,i)
            profit=max(profit,i-mini)
        return profit
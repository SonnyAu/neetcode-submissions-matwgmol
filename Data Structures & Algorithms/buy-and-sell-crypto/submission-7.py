class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = ans = curr = 0

        for r in range(len(prices)):

            if prices[r] < prices[l]:
                l = r
            elif prices[r] > prices[l]:
                ans = max(ans, prices[r] - prices[l])
            
        return ans

        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = curr = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                curr = prices[right] - prices[left]
                ans = max(ans, curr)
        return ans
        
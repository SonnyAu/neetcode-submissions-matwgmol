class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = curr = 0

        for i in range(1, len(prices)):
            if prices[left] > prices[i]:
                left = i
            else:
                curr = prices[i] - prices[left]
                ans = max(ans, curr)
        return ans
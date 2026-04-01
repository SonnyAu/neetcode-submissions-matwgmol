class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = left = 0

        for right in range(len(prices)):
            while prices[right] < prices[left]:
                left += 1

            ans = max(ans, prices[right] - prices[left])

        return ans
        
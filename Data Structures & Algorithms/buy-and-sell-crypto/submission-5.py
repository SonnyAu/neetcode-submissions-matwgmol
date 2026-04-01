class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = curr = left = 0

        for right in range(len(prices)):
            while prices[right] < prices[left]:
                left += 1
            
            ans = max(ans, prices[right] - prices[left])
            print(f"{prices[left]}, {prices[right]}")
        return ans
        
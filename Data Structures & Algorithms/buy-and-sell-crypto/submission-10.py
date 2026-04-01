class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = ans = 0
        '''

        '''
        for r in range(1, len(prices)):
            while prices[r] < prices[l]:
                print(prices[l], prices[r])
                l += 1
            else:
                ans = max(ans, prices[r] - prices[l])
            '''
            elif prices[r] > prices[l]:
                ans = max(ans, prices[r] - prices[l])
            '''

        return ans


        
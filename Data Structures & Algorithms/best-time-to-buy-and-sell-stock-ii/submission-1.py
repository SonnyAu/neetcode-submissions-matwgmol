class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, b):
            if i == len(prices):
                return 0

            if (i, b) in memo:
                return memo[(i, b)]
            res = dp(i + 1, b)

            if b:
                res = max(res, prices[i] + dp(i + 1, False))
            else:
                res = max(res, -prices[i] + dp(i + 1, True))
            memo[(i, b)] = res
            return res

        return dp(0, False)

        
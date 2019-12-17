class Solution:
    def maxProfit(self, prices) -> int:
        nlen = len(prices)
        if nlen <= 1:
            return 0
        dp = [0] * nlen
        dp[1] = max(dp[0], prices[1] - prices[0])
        for i in range(2, nlen):
            # 冷却
            dp[i] = max(dp[i - 1], dp[i])
            # 非冷却
            for j in range(i):
                if j >= 2:
                    dp[i] = max(dp[i], prices[i] - prices[j] + dp[j - 2])
                else:
                    dp[i] = max(dp[i], prices[i] - prices[j])

        return dp[-1]


slu = Solution()
print(slu.maxProfit([1,2]))

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        dp = [-1] * (amount + 1)
        for i in coins:
            if i <= amount:
                dp[i] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] >= 0:
                    if dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1]


slu = Solution()
print(slu.coinChange([370, 417, 408, 156, 143, 434, 168, 83, 177, 280, 117], 9953))

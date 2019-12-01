class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        coins = []
        while i * i <= n:
            coins.append(i*i)
            i += 1
        if n == 0:
            return 0
        if n < 0:
            return -1
        dp = [-1] * (n + 1)
        for i in coins:
            if i <= n:
                dp[i] = 1

        for i in range(1, n + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] >= 0:
                    if dp[i] == -1:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1]

slu = Solution()
print(slu.numSquares(6616))
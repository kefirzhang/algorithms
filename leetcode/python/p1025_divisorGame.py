class Solution:
    def divisorGame(self, N) -> bool:
        return N % 2 == 0

    def divisorGame2(self, N) -> bool:
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == 0:
                    dp[i] = 1

        return dp[-1] == 1


slu = Solution()
print(slu.divisorGame(5))

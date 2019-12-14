class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        n_2, n_3, n_5 = 0, 0, 0
        for i in range(1, n):
            minnum = min(dp[n_2] * 2, dp[n_3] * 3, dp[n_5] * 5)
            dp[i] = minnum

            if minnum == dp[n_2] * 2:
                n_2 += 1
            if minnum == dp[n_3] * 3:
                n_3 += 1
            if minnum == dp[n_5] * 5:
                n_5 += 1
            # print(minnum, n_2, n_3, n_5)
        return dp


slu = Solution()
print(slu.nthUglyNumber(10))

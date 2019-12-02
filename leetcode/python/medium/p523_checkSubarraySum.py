class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        m = len(nums)
        dp = [[0] * m for i in range(m)]

        for i, n in enumerate(nums):
            if i == 0:
                dp[0][i] = n
            else:
                dp[0][i] = n + dp[0][i - 1]
                if k == 0 and dp[0][i] == 0:
                    return True
                elif k != 0 and dp[0][i] % k == 0:
                    return True

        for i in range(1, m):
            for j in range(i + 1, m):
                dp[i][j] = dp[0][j] - dp[0][i - 1]
                if k == 0 and dp[i][j] == 0:
                    return True
                elif k != 0 and dp[i][j] % k == 0:
                    return True
        return False


slu = Solution()
print(slu.checkSubarraySum([0, 0], 0))

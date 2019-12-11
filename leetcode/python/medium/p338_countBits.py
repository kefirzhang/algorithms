class Solution:
    def countBits(self, num: int):
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i & 1 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[int(i / 2)]
        return dp


slu = Solution()
print(slu.countBits(10))

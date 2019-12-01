class Solution:
    def canPartition(self, nums) -> bool:
        if not nums:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        middle = int(total / 2)

        dp = [[False] * (middle + 1) for i in range(len(nums) + 1)]
        dp[0][0] = True
        # print(dp[0])
        for i in range(1, len(nums) + 1):
            for j in range(1, middle + 1):
                dp[i][j] = dp[i][j] or dp[i - 1][j]  # case 1 不用 nums[i]
                if j >= nums[i - 1]:
                    # print(j,nums[i-1])
                    dp[i][j] = (dp[i][j] or dp[i - 1][j - nums[i - 1]])
            # print(dp[i])
        return dp[len(nums)][middle]


slu = Solution()
print(slu.canPartition([1, 5, 11, 5]))

# dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]], (nums[i] <= j) 4

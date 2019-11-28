class Solution:
    def rob(self, nums) -> int:
        def robDp(subNums):
            if len(subNums) < 2:
                return subNums[0]
            dp = [0] * len(subNums)
            dp[0] = subNums[0]
            dp[1] = max(subNums[0], subNums[1])
            for i in range(2, len(subNums)):
                dp[i] = max(subNums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(robDp(nums[0:-1]), robDp(nums[1:]))


slu = Solution()
print(slu.rob([0,0]))

class Solution:
    helper = {}

    def maxCoins(self, nums) -> int:
        if self.helper.__contains__(tuple(nums)):
            return self.helper[tuple(nums)]
        nlen = len(nums)
        if nlen == 1:
            return nums[0]
        max_coin = 0
        for i in range(nlen):
            if i == 0:
                left = 1
            else:
                left = nums[i - 1]
            if i == nlen - 1:
                right = 1
            else:
                right = nums[i + 1]

            max_coin = max(max_coin, left * nums[i] * right + self.maxCoins(nums[:i] + nums[i + 1:]))
        self.helper[tuple(nums)] = max_coin
        return max_coin


# dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
import time

print(time.strftime("%Y-%m-%d %H:%M:%S"))
slu = Solution()
print(slu.maxCoins([8, 2, 6, 8, 9, 8, 1, 4, 1, 5, 3, 0, 7, 7, 0, 4, 2, 2, 5, 5]))
print(slu.helper)
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# [3,1,5,8]

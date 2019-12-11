class Solution:
    def canJump(self, nums) -> bool:
        max_distance = nums[0]
        for i in range(1, len(nums)):
            if max_distance < i:
                break
            max_distance = max(max_distance, i + nums[i])
        return max_distance >= (len(nums)-1)

    def canJump2(self, nums) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i, n in enumerate(nums):
            if dp[i] is False:
                continue
            for j in range(1, n + 1):
                if i + j < len(nums):
                    dp[i + j] = True

        return dp[-1]


slu = Solution()
print(slu.canJump([2, 0, 0]))

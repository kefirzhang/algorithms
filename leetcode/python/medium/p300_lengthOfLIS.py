class Solution:
    def lengthOfLIS(self, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0
        dp = [1] * length
        maxlength = 1
        for i in range(1, length):

            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxlength = max(dp[i], maxlength)
        return maxlength


slu = Solution()
print(slu.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

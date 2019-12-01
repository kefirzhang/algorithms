class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2

        dp = [0] * (total + 1)

        for i in nums:
            dp[i] = True
            


        return True


slu = Solution()
print(slu.canPartition([1, 5, 11, 5]))

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return int((n + 1) * (n / 2) - sum(nums))


slu = Solution()
print(slu.missingNumber([3, 0, 1]))

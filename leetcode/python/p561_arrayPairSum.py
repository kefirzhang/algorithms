class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        i = 0
        total = 0
        while i < len(nums):
            total += nums[i]
            i += 2
        return total


slu = Solution()
print(slu.arrayPairSum([1, 4, 3, 2]))

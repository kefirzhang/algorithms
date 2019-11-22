class Solution:
    def pivotIndex(self, nums) -> int:
        total = sum(nums)
        left = 0
        right = total
        for i, n in enumerate(nums):
            if i > 0:
                left = left + nums[i - 1]
            right = right - nums[i]
            if left == right:
                return i

        return -1


slu = Solution()
print((slu.pivotIndex([1, 7, 3, 6, 5, 6])))

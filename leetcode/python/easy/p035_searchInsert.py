class Solution:
    def searchInsert(self, nums, target):
        for i, n in enumerate(nums):
            if target <= n:
                return i
        return i + 1


slu = Solution()
print(slu.searchInsert([1, 3, 5, 6], 7))

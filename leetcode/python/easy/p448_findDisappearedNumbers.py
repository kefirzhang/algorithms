class Solution:
    def findDisappearedNumbers(self, nums):
        helper = []
        for i, n in enumerate(nums):
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for i, n in enumerate(nums):
            if n > 0:
                helper.append(i + 1)
        return helper


slu = Solution()
print(slu.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

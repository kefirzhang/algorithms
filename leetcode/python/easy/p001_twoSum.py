class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            find = target - num
            if find in dict:
                return [dict[find]] + [index]
            dict[num] = index


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))

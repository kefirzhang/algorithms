class Solution:
    def findRelativeRanks(self, nums):
        a = sorted(nums, reverse=True)
        b = {}

        for i, n in enumerate(a):
            if i == 0:
                b[n] = "Gold Medal"
            elif i == 1:
                b[n] = "Silver Medal"
            elif i == 2:
                b[n] = "Bronze Medal"
            else:
                b[n] = str(i + 1)
        for i, n in enumerate(nums):
            nums[i] = b[n]
        return nums


slu = Solution()
print(slu.findRelativeRanks([10, 3, 8, 9, 4]))

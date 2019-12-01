class Solution:
    def __init__(self):
        self.helper = {}

    def findTargetSumWays(self, nums, S: int) -> int:
        if not nums:
            return 0
        if self.helper.__contains__(tuple([len(nums), S])):
            return self.helper[tuple([len(nums), S])]
        if len(nums) == 1:
            if S == nums[0] and S == -nums[0]:
                self.helper[tuple([len(nums), S])] = 2
                return 2
            elif S == nums[0] or S == -nums[0]:
                self.helper[tuple([len(nums), S])] = 1
                return 1
            else:
                self.helper[tuple([len(nums), S])] = 0
                return 0

        num = self.findTargetSumWays(nums[:-1], S + nums[-1]) + self.findTargetSumWays(nums[:-1], S - nums[-1])
        self.helper[tuple([len(nums), S])] = num
        return num


slu = Solution()
print(slu.findTargetSumWays([2, 20, 24, 38, 44, 21, 45, 48, 30, 48, 14, 9, 21, 10, 46, 46, 12, 48, 12, 38], 48))

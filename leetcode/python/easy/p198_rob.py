class Solution:
    def __init__(self):
        self.helper = {}

    def rob(self, nums) -> int:
        length = len(nums)
        if self.helper.__contains__(length):
            return self.helper[length]

        if length == 0:
            return 0
        elif length == 1:
            return nums[0]

        num = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        self.helper[length] = num
        return num


slu = Solution()
print(slu.rob([2, 7, 9, 3, 1]))

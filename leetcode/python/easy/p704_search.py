class Solution:
    def search(self, nums, target):
        if len(nums) == 1 and nums[0] != target:
            return -1
        middle = int(len(nums) / 2)

        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            pos = self.search(nums[middle:], target)
            if pos == -1:
                return -1
            else:
                return middle + self.search(nums[middle:], target)
        else:
            return self.search(nums[0:middle], target)


slu = Solution()
print(slu.search([-1, 0, 3, 5, 9, 12], 2))

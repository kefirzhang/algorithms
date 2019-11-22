class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        new_length = 0
        i = 0
        while i < length:
            if nums[i] != val:
                nums[new_length] = nums[i]
                new_length += 1
            i += 1
        return new_length


slu = Solution()
print(slu.removeElement([0,1,2,2,3,0,4,2], 2))

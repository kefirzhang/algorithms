class Solution:
    def removeDuplicates(self, nums):

        length = len(nums)
        if length <= 1:
            return length
        num = 1
        i = 0
        j = 1
        while j < length:
            if nums[i] != nums[j]:
                num += 1
                nums[num - 1] = nums[j]
                i = j
            j += 1
        return num


slu = Solution()
print(slu.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

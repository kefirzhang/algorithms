class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        helper = nums[:]
        helper.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != helper[i] and nums[j] != helper[j]:
                break
            if nums[i] == helper[i]:
                i += 1
            if nums[j] == helper[j]:
                j -= 1
        if j <= i:
            return 0
        else:
            return j - i + 1


slu = Solution()
print(slu.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

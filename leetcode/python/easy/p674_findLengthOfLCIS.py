class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        i, length = 0, len(nums)
        if length <= 1:
            return length
        max_continue, cur_continue = 1, 1
        while i < length - 1:
            if nums[i] < nums[i + 1]:
                cur_continue += 1
            else:
                max_continue = max(max_continue, cur_continue)
                cur_continue = 1
            i += 1
        max_continue = max(max_continue, cur_continue)
        return max_continue


slu = Solution()
print(slu.findLengthOfLCIS([1, 3, 5, 4, 7]))

class Solution:
    def findLHS(self, nums) -> int:
        nums.sort()
        pre_num, pre_length = -1, 0
        cur_num, cur_length = -1, 0
        i = 0
        max_length = 0
        while i < len(nums):
            if nums[i] == cur_num:
                cur_length += 1
            else:
                if cur_num == pre_num + 1:
                    max_length = max(max_length, cur_length + pre_length)

                pre_num = cur_num
                pre_length = cur_length

                cur_num = nums[i]
                cur_length = 1
            i += 1
        if cur_num == pre_num + 1:
            max_length = max(max_length, cur_length + pre_length)
        return max_length


slu = Solution()
print(slu.findLHS([1, 1, 1, 1, 2]))

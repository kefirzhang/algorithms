class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        max_long = 0
        helper_set = set(nums)
        for i in helper_set:
            if i - 1 not in helper_set:
                cur_num = i
                cur_long = 1
                while cur_num + 1 in helper_set:
                    cur_num += 1
                    cur_long += 1
                else:
                    max_long = max(max_long, cur_long)
        max_long = max(max_long, cur_long)
        return max_long


slu = Solution()
print(slu.longestConsecutive([100, 4, 200, 1, 3, 2]))

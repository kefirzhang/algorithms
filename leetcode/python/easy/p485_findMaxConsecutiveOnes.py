class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_i = 0
        cur_i = 0
        for i in nums:
            if i == 0:
                max_i = max(cur_i, max_i)
                cur_i = 0
            else:
                cur_i += 1
        max_i = max(cur_i, max_i)
        return max_i


slu = Solution()
print(slu.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

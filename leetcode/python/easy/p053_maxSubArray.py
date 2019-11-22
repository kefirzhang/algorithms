class Solution:
    def maxSubArray(self, nums):
        i = 0
        j = 1
        max_total = nums[i]
        pre_total = nums[i]  # 临时总数 必须大于0
        length = len(nums)
        while j < length:
            if pre_total < 0:
                pre_total = nums[j]
            else:
                pre_total += nums[j]
            max_total = max(max_total, pre_total)
            j += 1

        return max_total


slu = Solution()
print(slu.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

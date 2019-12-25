class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        nlen = len(nums)
        dp_max = [0] * nlen
        dp_min = [0] * nlen
        dp_max[0] = dp_min[0] = max_num = nums[0]
        for i in range(1, nlen):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            max_num = max(max_num, dp_max[i])
        # print(dp_max)
        return max_num


slu = Solution()
print(slu.maxProduct([-1]))

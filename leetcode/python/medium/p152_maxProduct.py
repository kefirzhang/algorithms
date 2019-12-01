class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return False
        cur_max = nums[0]
        cur_min = nums[0]
        g_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i] * cur_max, nums[i] * cur_min)
            cur_min = min(nums[i], nums[i] * cur_min)
            g_max = max(cur_max, g_max)
            print(cur_max, cur_min, g_max)
        return g_max


slu = Solution()
print(slu.maxProduct([-1, -2, -9, -6]))

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums or not k:
            return []

        res = []
        nlen = len(nums)
        for i in range(nlen - k + 1):
            res.append(max(nums[i:i + k]))
        return res


slu = Solution()
print(slu.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

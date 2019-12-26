class Solution:
    def maxSlidingWindow2(self, nums, k: int):
        if not nums or not k:
            return []

        res = []
        nlen = len(nums)
        for i in range(nlen - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        if n * k == 0:
            return []
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(nums[i], left[i - 1])
            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(nums[j], right[j + 1])
        res = []
        for i in range(n - k + 1):
            res.append(max(right[i], left[i + k - 1]))
        return res


slu = Solution()
print(slu.maxSlidingWindow([-7, -8, 7, 5, 7, 1, 6, 0], 4))

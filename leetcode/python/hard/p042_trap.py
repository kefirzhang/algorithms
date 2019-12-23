class Solution:
    def trap(self, height) -> int:
        nlen = len(height)
        max_left = [0] * nlen
        max_right = [0] * nlen
        for i in range(1, nlen):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(nlen - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        res = 0
        for i in range(nlen):
            if height[i] < max_left[i] and height[i] < max_right[i]:
                res += min(max_left[i], max_right[i]) - height[i]

        return res


slu = Solution()
print(slu.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

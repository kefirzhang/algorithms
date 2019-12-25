class Solution:
    def largestRectangleArea2(self, heights) -> int:
        nlen = len(heights)
        dp = [[0 for _ in range(nlen)] for _ in range(nlen)]
        max_area = 0
        for i in range(nlen):
            dp[i][i] = heights[i]
            max_area = max(max_area, dp[i][i])
        for i in range(nlen):
            for j in range(i + 1, nlen):
                dp[i][j] = min(dp[j][j], int(dp[i][j - 1] / (j - i))) * (j - i + 1)
                max_area = max(max_area, dp[i][j])
        return max_area

    def largestRectangleArea(self, heights) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top_idx = stack.pop()
                area = (i - stack[-1] - 1) * heights[top_idx]
                # print(i, stack, stack[-1], top_idx, heights[top_idx])
                max_area = max(max_area, area)
            stack.append(i)
        return max_area


slu = Solution()
print(slu.largestRectangleArea([2, 1, 5, 6, 2, 3]))

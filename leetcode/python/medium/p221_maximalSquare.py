class Solution:
    def maximalSquare(self, matrix) -> int:
        if (len(matrix)) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for i in range(n)]
        maxLength = 0

        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = int(matrix[i][j]) + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    maxLength = max(maxLength, dp[i][j])
        return maxLength * maxLength


slu = Solution()
print(slu.maximalSquare([["1", "0", "1", "1", "0", "1"], ["1", "1", "1", "1", "1", "1"],
                          ["0", "1", "1", "0", "1", "1"], ["1", "1", "1", "0", "1", "0"],
                          ["0", "1", "1", "1", "1", "1"], ["1", "1", "0", "1", "1", "1"]]))

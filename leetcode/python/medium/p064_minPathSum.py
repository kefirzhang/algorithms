class Solution:
    def minPathSum(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for i in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[n - 1][m - 1]


slu = Solution()
print(slu.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))

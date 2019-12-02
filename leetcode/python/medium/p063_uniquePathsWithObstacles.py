class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[0][i] == 1 or dp[0][i - 1] == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        for i in range(1, n):
            if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[n - 1][m - 1]


slu = Solution()
print(slu.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))

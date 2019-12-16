class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        if m == 0:
            return 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    dp[i][j][0] = dp[i][j + 1][0] + 1
                    dp[i][j][1] = dp[i + 1][j][1] + 1
        max_height = m
        while max_height > 0:
            for i in range(m - max_height + 1):
                for j in range(n - max_height + 1):
                    if dp[i][j][0] >= max_height and dp[i][j][1] >= max_height:
                        if dp[i + max_height - 1][j][0] >= max_height and dp[i][j + max_height - 1][1] >= max_height:
                            return max_height * max_height
            max_height -= 1
        return 0


slu = Solution()
print(slu.largest1BorderedSquare([[1,1,0,0]]))

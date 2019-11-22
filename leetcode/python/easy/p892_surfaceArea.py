class Solution:
    def surfaceArea(self, grid) -> int:
        N = len(grid)
        total = 0
        for i, m in enumerate(grid):
            # print(i, m, "first")
            for j, n in enumerate(m):
                if grid[i][j] > 0:
                    total += grid[i][j] * 6 - (grid[i][j] - 1) * 2
                    for nr, nc in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            if grid[nr][nc] > 0:
                                total -= min(grid[nr][nc], grid[i][j])
        return total


slu = Solution()
print(slu.surfaceArea([[1, 0], [0, 2]]))

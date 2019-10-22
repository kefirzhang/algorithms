class Solution:
    def islandPerimeter(self, grid) -> int:
        r = len(grid)
        c = len(grid[0])
        num = 0
        for i, m in enumerate(grid):
            for j, n in enumerate(m):
                neighbor = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                if grid[i][j] == 1:
                    num += 4
                    for k in neighbor:
                        if 0 <= k[0] < r and 0 <= k[1] < c:
                            if grid[k[0]][k[1]] == 1:
                                num -= 1

        return num


slu = Solution()
print(slu.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))

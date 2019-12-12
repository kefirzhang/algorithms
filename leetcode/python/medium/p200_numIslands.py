class Solution:
    def numIslands(self, grid) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        mark = [[False for i in range(n)] for i in range(m)]
        res = 0

        def doMark(row, col):
            mark[row][col] = True
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == "1" and mark[new_row][new_col] is False:
                    doMark(new_row, new_col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and mark[i][j] is False:
                    doMark(i, j)
                    res += 1

        return res


slu = Solution()
print(slu.numIslands([]))

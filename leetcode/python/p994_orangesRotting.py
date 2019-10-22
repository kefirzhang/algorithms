class Solution:
    def orangesRotting(self, grid) -> int:
        r = len(grid)
        c = len(grid[0])
        times = 1
        is_change = False

        while times < r + c:
            is_all_bad = True
            for x in range(r):
                for y in range(c):
                    dots = [[x, y - 1], [x, y + 1], [x + 1, y], [x - 1, y]]
                    # print(r, c, x, y, grid[x][y], dots)

                    # continue
                    if grid[x][y] == 1:
                        is_all_bad = False
                    elif grid[x][y] == 2:
                        for dot in dots:
                            if 0 <= dot[0] < r and 0 <= dot[1] < c:
                                if grid[dot[0]][dot[1]] == 1:
                                    grid[dot[0]][dot[1]] = 3
                                    is_change = True
            for x in range(r):
                for y in range(c):
                    if grid[x][y] == 3:
                        grid[x][y] = 2

            if is_all_bad:
                if is_change:
                    return times
                else:
                    return 0
            times += 1
        return -1


slu = Solution()
print(slu.orangesRotting([[0,2]]))

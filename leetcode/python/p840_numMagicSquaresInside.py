class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        def isMagic(i, j):
            nodes = [
                grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],
                grid[i][j-1], grid[i][j], grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1],
            ]
            if (len(set(nodes)) == 9 and max(nodes) == 9 and min(nodes) == 1) is False:
                return False


            sums = [
                # row
                grid[i - 1][j - 1]+grid[i - 1][j]+grid[i - 1][j + 1],
                grid[i][j - 1]+grid[i][j]+grid[i][j + 1],
                grid[i + 1][j - 1]+grid[i + 1][j]+grid[i + 1][j + 1],
                # colum
                grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1],
                grid[i-1][j] + grid[i][j] + grid[i+1][j],
                grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1],

                # 对角

                grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1],
                grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1],
            ]
            if min(sums) == max(sums):
                return True
            else:
                return False

        r = len(grid)
        c = len(grid[0])
        total = 0
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if isMagic(i, j):
                    total += 1

        return total


slu = Solution()
print(slu.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))

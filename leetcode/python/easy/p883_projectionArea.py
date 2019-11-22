class Solution:
    def projectionArea(self, grid) -> int:
        xy, yz, xz = set(), set(), set()

        for i, m in enumerate(grid):
            for j, n in enumerate(m):
                if n == 0:
                    continue
                xy.add(tuple([i, j]))
                for k in range(n):
                    yz.add(tuple([i, k]))
                    xz.add(tuple([j, k]))
        return len(xy) + len(yz) + len(xz)


slu = Solution()
print(slu.projectionArea([[1,0],[0,2]]))

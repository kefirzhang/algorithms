class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        helper = [[]] * (R + C)
        for i in range(R):
            for j in range(C):
                distance = abs(i - r0) + abs(j - c0)
                helper[distance] = helper[distance] + [[i, j]]
        arr = []
        for tmp_arr in helper:
            arr = arr + tmp_arr
        return arr


slu = Solution()
print(slu.allCellsDistOrder(10, 10, 5, 5))

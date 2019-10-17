class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        # 0,0 0,1 0,2 0,3
        for i in range(c):
            x = i
            y = 0
            pre = matrix[y][x]
            while x < c and y < r:
                if pre != matrix[y][x]:
                    return False
                x += 1
                y += 1
        for j in range(1, r):
            x = 0
            y = j
            pre = matrix[y][x]
            while x < c and y < r:
                if pre != matrix[y][x]:
                    return False
                x += 1
                y += 1

        return True


slu = Solution()
print(slu.isToeplitzMatrix([
    [1, 2, 3, 4],
    [5, 1, 2, 2],
    [9, 5, 1, 2]
]))

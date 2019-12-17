class Solution:
    def rotate2(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        new_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n - i - 1] = matrix[i][j]
        matrix = new_matrix

    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        print(matrix)


slu = Solution()
print(slu.rotate([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]))

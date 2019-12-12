class Solution:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def search(self, board, word, mark, index, row, col, m, n):
        if index == len(word) - 1:
            return board[row][col] == word[-1]
        if word[index] == board[row][col]:
            mark[row][col] = True
            for direct in self.directions:
                new_row = row + direct[0]
                new_col = col + direct[1]
                if 0 <= new_row < m and 0 <= new_col < n and mark[new_row][new_col] is False:
                    if self.search(board, word, mark, index + 1, new_row, new_col, m, n):
                        return True
            mark[row][col] = False
        return False

    def exist(self, board, word) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[False for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if self.search(board, word, mark, 0, i, j, m, n):
                    return True
        return False


slu = Solution()
print(slu.exist([["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]],
                "aaaaaaaaaaaaa"))

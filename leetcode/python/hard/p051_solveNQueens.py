class Solution:
    res = []

    def solveNQueens(self, n: int):
        board = [['.'] * n for i in range(n)]
        self.backTrack(board, 0)

        return self.res

    def backTrack(self, board, row):
        if row == len(board):
            self.res.append(board)
            return
        n = len(board[row])
        for i in range(n):
            if self.isVaild(board, row, i) is False:
                continue
            board[row][i] = 'Q'
            self.backTrack(board, row + 1)
            board[row][i] = '.'

    def isVaild(self, board, row, col):

        # 左上方
        m, n = row, col
        while m >= 0 and n >= 0:
            if board[m][n] == 'Q':
                return False
            m -= 1
            n -= 1
        # 正上方
        m = row
        while m >= 0:
            if board[m][col] == 'Q':
                return False
            m -= 1
            # 右上方
        m, n = row, len(board)
        while m >= 0 and n >= col:
            if board[m][col] == 'Q':
                return False
            m -= 1
            n -= 1

        return True


slu = Solution()
print(slu.solveNQueens(4))

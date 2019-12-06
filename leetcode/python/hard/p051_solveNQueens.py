class Solution:
    def __init__(self):
        self.ret = []

    def solveNQueens(self, n: int):
        board = [['.' for j in range(n)] for i in range(n)]
        self.backTrack(board, 0)
        return self.ret

    def backTrack(self, board, row):
        if row == len(board):
            tmp = ["".join(x) for x in board]
            self.ret.append(tmp)
            return
        n = len(board[row])
        for col in range(n):
            if self.isVaild(board, row, col) is False:
                continue
            board[row][col] = 'Q'
            self.backTrack(board, row + 1)
            board[row][col] = '.'

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
        m, n = row, col
        while m >= 0 and n < len(board[0]):
            if board[m][n] == 'Q':
                return False
            m -= 1
            n += 1

        return True


slu = Solution()
print(slu.solveNQueens(4))
# [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

class Solution:
    def numRookCaptures(self, board) -> int:
        ans = 0
        r = len(board)
        c = len(board[0])
        x, y = -1, -1
        for i in range(0, r):
            for j in range(0, c):
                if board[i][j] == "R":
                    x, y = i, j
                    break
        if x == -1:
            return ans
        l_y = y
        while l_y >= 0:
            if board[x][l_y] == "B":
                break
            elif board[x][l_y] == "p":
                ans += 1
                break
            l_y -= 1

        r_y = y
        while r_y < c:
            if board[x][r_y] == "B":
                break
            elif board[x][r_y] == "p":
                ans += 1
                break
            r_y += 1

        d_x = x
        while d_x >= 0:
            if board[d_x][y] == "B":
                break
            elif board[d_x][y] == "p":
                ans += 1
                break
            d_x -= 1

        u_x = x
        while u_x < r:
            if board[u_x][y] == "B":
                break
            elif board[u_x][y] == "p":
                ans += 1
                break
            u_x += 1

        return ans


slu = Solution()
print(slu.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
                          ))

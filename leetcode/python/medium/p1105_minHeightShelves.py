class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        length = len(books)
        dp = [1000000] * (length + 1)
        dp[0] = 0
        for i in range(1, length + 1):
            tmp_width, h, j = 0, 0, i
            while j > 0:
                h = max(h, books[j - 1][1])
                tmp_width += books[j - 1][0]
                if tmp_width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j - 1] + h)
                j -= 1
        return dp[-1]


slu = Solution()
print(slu.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))

class Solution:
    def findLength(self, A, B) -> int:
        A = [0] + A
        B = [0] + B
        m, n = len(A), len(B)
        dp = [[0] * m for i in range(n)]
        max_length = 0
        for i in range(1, n):
            for j in range(1, m):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length


slu = Solution()
print(slu.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))

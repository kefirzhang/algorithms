class Solution: # 可以用hash 替换list数组空间
    def longestArithSeqLength(self, A) -> int:
        length = len(A)
        dp = [[0 for _ in range(20000)] for _ in range(length)]
        max_length = 0
        for i in range(1, length):
            for j in range(i):
                distance = A[i] - A[j] + 10000
                dp[i][distance] = max(dp[j][distance] + 1, dp[i][distance])
                max_length = max(max_length, dp[i][distance])
        return max_length + 1


slu = Solution()
print(slu.longestArithSeqLength([20,1,15,3,10,5,8]))

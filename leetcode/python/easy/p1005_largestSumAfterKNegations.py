class Solution:
    def largestSumAfterKNegations(self, A, K) -> int:
        for i in range(K):
            A.sort()
            A[0] = -A[0]
        return sum(A)


slu = Solution()
print(slu.largestSumAfterKNegations([4, 2, 3], 1))

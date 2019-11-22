class Solution:
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A


slu = Solution()
print(slu.sortedSquares([-4, -1, 0, 3, 10]))

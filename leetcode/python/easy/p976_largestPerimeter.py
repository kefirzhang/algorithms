class Solution:
    def largestPerimeter(self, A) -> int:
        A.sort()
        length = len(A)
        i = length - 3
        while i >= 0:
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
            i -= 1

        return 0


slu = Solution()
print(slu.largestPerimeter([3, 2, 3, 4]))

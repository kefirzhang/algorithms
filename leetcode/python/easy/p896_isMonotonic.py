class Solution:
    def isMonotonic(self, A) -> bool:
        if len(A) <= 1:
            return True
        crease = True
        increase = True
        i, end = 0, len(A) - 1
        while i < end:
            if A[i] < A[i + 1]:
                increase = False

            if A[i] > A[i + 1]:
                crease = False
            i += 1
        return increase or crease


slu = Solution()
print(slu.isMonotonic([1, 2, 2, 3]))

class Solution:
    def validMountainArray(self, A) -> bool:
        if len(A) < 3:
            return False
        index = A.index(max(A))
        if index == 0 or index == len(A) - 1:
            return False
        i = index
        j = index
        while i > 0:
            if A[i] <= A[i - 1]:
                return False
            i -= 1
        while j < len(A) - 1:
            if A[j] <= A[j + 1]:
                return False
            j += 1
        return True


slu = Solution()
print(slu.validMountainArray([1, 2, 1, 3, 1]))

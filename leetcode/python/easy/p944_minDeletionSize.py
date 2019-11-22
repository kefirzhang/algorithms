class Solution:
    def minDeletionSize(self, A) -> int:
        r = len(A)
        c = len(A[0])
        ans = 0
        for j in range(c):
            for i in range(r-1):
                if A[i][j] > A[i+1][j]:
                    ans += 1
                    break
        return ans

slu = Solution()
print(slu.minDeletionSize(["zyx","wvu","tsr"]))
class Solution:
    def sortArrayByParity(self, A):
        odd_p, even_p = 0, len(A) - 1

        while odd_p < even_p:
            if A[odd_p] & 1 != 1:  # 奇数
                odd_p += 1
            elif A[even_p] & 1 != 0:  # 偶数：
                even_p -= 1
            else:
                A[odd_p], A[even_p] = A[even_p], A[odd_p]
                odd_p += 1
                even_p -= 1
        return A


slu = Solution()
print(slu.sortArrayByParity([3, 1, 2, 4]))

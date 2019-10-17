class Solution:
    def transpose(self, A):
        r = len(A)
        c = len(A[0])
        helper = []
        for i in range(c):
            i_helper = []
            for j in range(r):
                i_helper.append(A[j][i])
            helper.append(i_helper)

        return helper


slu = Solution()
print(slu.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

class Solution:
    def flipAndInvertImage(self, A):
        def transfer(a_list):
            helper = []
            while len(a_list) != 0:
                value = 1 if a_list.pop() == 0 else 0
                helper.append(value)
            return helper

        for i, n in enumerate(A):
            A[i] = transfer(n)
        return A


slu = Solution()
print(slu.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))

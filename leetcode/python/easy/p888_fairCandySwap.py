class Solution:
    def fairCandySwap(self, A, B):
        sum_a = sum(A)
        sum_b = sum(B)
        set_b = set(B)
        target = int((sum_a + sum_b) / 2)
        for i in A:
            j = target - (sum_a - i)
            if j in set_b:
                return [i, j]


slu = Solution()
print(slu.fairCandySwap([1, 2, 5], [2, 4]))

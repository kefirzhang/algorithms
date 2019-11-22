class Solution:
    def trailingZeroes(self, n):
        res = 0
        while n >= 5:
            res += int(n/5)
            n = int(n/5)
        return res
slu = Solution()
print(slu.trailingZeroes(30))

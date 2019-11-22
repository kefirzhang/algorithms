class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        for opt in ops:
            m = min(m, opt[0])
            n = min(n, opt[1])

        return m * n


slu = Solution()
print(slu.maxCount(3, 3, [[2, 2], [3, 3]]))

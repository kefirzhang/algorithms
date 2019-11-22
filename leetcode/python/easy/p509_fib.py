class Solution:
    def fib(self, n) -> int:
        helper = {}
        helper[0] = 0
        helper[1] = 1
        for i in range(2, n + 1):
            helper[i] = helper[i - 1] + helper[i - 2]
        return helper[n]


slu = Solution()
print(slu.fib(10))

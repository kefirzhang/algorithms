class Solution:
    def tribonacci(self, n: int) -> int:
        helper = [0, 1, 1]
        if n < 3:
            return helper[n]
        for i in range(3, n + 1):
            helper.append(helper[i - 1] + helper[i - 2] + helper[i - 3])

        return helper[n]


slu = Solution()
print(slu.tribonacci(4))

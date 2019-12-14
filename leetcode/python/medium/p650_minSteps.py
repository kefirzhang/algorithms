class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        for i in range(int(n / 2), 1, -1):
            if n % i == 0:
                return int(self.minSteps(i) + n / i)

        return int(n)  # 如果是素数 返回本身


slu = Solution()
print(slu.minSteps(3))


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 4 or n == 1:
            return True
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(int(n / 4))


slu = Solution()
print(slu.isPowerOfFour(4))

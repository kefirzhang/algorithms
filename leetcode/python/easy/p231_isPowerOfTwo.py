class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 2 or n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(int(n / 2))


slu = Solution()
print(slu.isPowerOfTwo(1))

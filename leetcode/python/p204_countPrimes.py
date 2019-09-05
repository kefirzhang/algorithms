import math
class Solution:
    def isPrime(self, n):
        if n <= 3:
            return n > 1
        if n % 2 == 0:
            return False
        i = 3
        middle = int(math.sqrt(n))
        while i <= middle:
            if n % i == 0:
                return False
            i += 2
        return True

    def countPrimes(self, n):
        total = 0
        pre = min(n, 5)
        for i in range(1, pre):
            if self.isPrime(i):
                total += 1
        i = 6
        while i <= n:
            if self.isPrime(i - 1):
                total += 1
            if i + 1 < n and self.isPrime(i + 1):
                total += 1
            i += 6
        return total


slu = Solution()
print(slu.countPrimes(999983))

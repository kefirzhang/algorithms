import math


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isPrime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            for i in range(2, math.ceil(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True

        ans = 0
        while L <= R:
            str = bin(L)
            if isPrime(str.count("1")):
                ans += 1
            # print(L, str, str.count("1"), isPrime(str.count("1")))
            L += 1

        return ans


slu = Solution()
print(slu.countPrimeSetBits(567, 607))

import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n < 3:
            return 1
        def isPrime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for i in range(2, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        def factory(num):

            if num <= 1:
                return num
            return num * factory(num - 1) % (10 ** 9 + 7)

        prime_num = 0
        for i in range(1, n + 1):

            if isPrime(i):
                prime_num += 1

        return factory(prime_num) * factory(n - prime_num) % (10 ** 9 + 7)


slu = Solution()
print(slu.numPrimeArrangements(5))

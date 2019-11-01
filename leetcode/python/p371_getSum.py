class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            print(a,b)
            tmp = a ^ b
            b = (a & b) << 1
            a = tmp
        return a


slu = Solution()
print(slu.getSum(-1, 1))

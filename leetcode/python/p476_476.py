class Solution:
    def findComplement(self, num: int) -> int:
        num2 = 1
        num1 = num
        while num > 0:
            num = num >> 1
            num2 = num2 << 1
        num2 -= 1
        return num2 ^ num1

slu = Solution()
print(slu.findComplement(5))
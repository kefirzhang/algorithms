class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        helper = []
        for i in range(1, num):
            if num % i == 0:
                helper.append(i)
        return num == sum(helper)

    def checkPerfectNumber2(self, num: int) -> bool:
        helper = []
        for i in range(1, num):
            if num % i == 0:
                helper.append(i)
        return num == sum(helper)


slu = Solution()
print(slu.checkPerfectNumber(25))

import math
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        symbol = "" if num >= 0 else "-"
        num = abs(num)
        ret = ""
        while num > 0:
            add = num % 7
            ret = str(add) + ret
            num = math.floor(num / 7)

        return symbol + ret
slu = Solution()
print(slu.convertToBase7(-100))

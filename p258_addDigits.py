class Solution:
    def addDigits(self, num: int) -> int:
        ret = num
        while ret >= 10:
            tmp_ret = 0
            for i in list(str(ret)):
                tmp_ret += int(i)
            ret = tmp_ret
        return ret


slu = Solution()
print(slu.addDigits(1089))

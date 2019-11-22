class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry, ret = 0, ""
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                cur = int(num1[i]) + int(num2[j]) + carry
                if cur >= 10:
                    carry = 1
                    cur = cur % 10
                else:
                    carry = 0
                ret = str(cur) + ret
            elif i >= 0:
                cur = int(num1[i]) + carry
                if cur >= 10:
                    carry = 1
                    cur = cur % 10
                else:
                    carry = 0
                ret = str(cur) + ret
            elif j >= 0:
                cur = int(num2[j]) + carry
                if cur >= 10:
                    carry = 1
                    cur = cur % 10
                else:
                    carry = 0
                ret = str(cur) + ret
            i -= 1
            j -= 1
        if carry == 1:
            ret = str(carry) + ret
        return ret


slu = Solution()
print(slu.addStrings("0", "0"))

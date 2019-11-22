class Solution:
    def addBinary(self, a, b):
        carry = 0
        c = ""
        while a != "" or b != "":
            a = str((a, 0)[a == ""])
            b = str((b, 0)[b == ""])
            p = int(a[-1]) + int(b[-1]) + carry
            carry = int(p / 2)
            p = p % 2
            c = str(p) + c
            a = a[:-1]
            b = b[:-1]
        if carry > 0:
            c = str(carry) + c

        return c


slu = Solution()
print(slu.addBinary("11110111110", "11110111110"))
